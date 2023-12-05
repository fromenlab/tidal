// Serial processing variables
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing
boolean newData = false;

//============

void setup() {
    Serial.begin(38400);
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        checkType();
        newData = false;
    }
}

//============

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    // char startMarker = ''; // No start marker
    char endMarker = '\r';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();
        recvInProgress = true;

        if (recvInProgress == true) {
            if (rc != '\r') {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        // else if (rc == startMarker) {
        //     recvInProgress = true;
        // }
    }
}


void checkType() {
    switch (tempChars[0])
    {
    case '?':
        parseQuery();
        break;
    case 'D':
    // Run this for any data query
        sendConfirmation();
        for (size_t i = 0; i < 1000; i++)
        {
            delay(10);
            Serial.write(highByte(i));
            Serial.write(lowByte(i));
        }
        sendTermination();
        break;
    default:
        printInvalid();
        break;
    }
}

void sendConfirmation() {
    Serial.write(0x00);
}

void sendTermination() {
    Serial.write(0xff);
    Serial.write(0xff);
}

void printInvalid() {
    Serial.println(F("Invalid command"));
}

void parseQuery() {
    if (strcmp(tempChars, "?") == 0)
        {
            Serial.print(F("OK-Flow\r"));
        }
         else
        {
            printInvalid();
        }
}