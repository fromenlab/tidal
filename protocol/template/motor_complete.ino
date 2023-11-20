
// Motor control parameters
// int (*p)[5][500];

// Maneuver arrays
const PROGMEM unsigned int identity[500] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

const PROGMEM unsigned int stored_inhale[5][500] = {
  $sub_inhale_ru,
  $sub_inhale_rm,
  $sub_inhale_rl,
  $sub_inhale_lu,
  $sub_inhale_ll
  };

const PROGMEM unsigned int stored_exhale[5][500] = {
  $sub_exhale_ru,
  $sub_exhale_rm,
  $sub_exhale_rl,
  $sub_exhale_lu,
  $sub_exhale_ll
  };

#define idarr {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
#define idarr1000 {1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000}

unsigned int delays[][500] = {
  idarr1000,
  idarr1000,
  idarr1000,
  idarr1000,
  idarr1000
};

// Default parameters
int inhale = 1;
int exhale = -1;

#define NUM_STEPPERS 5
int rul = 0;
int rml = 1;
int rll = 2;
int lul = 3;
int lll = 4;

#define RUL_DIR_PIN          36
#define RUL_STEP_PIN         37

#define RML_DIR_PIN          40
#define RML_STEP_PIN         41

#define RLL_DIR_PIN          44
#define RLL_STEP_PIN         45

#define LUL_DIR_PIN          48
#define LUL_STEP_PIN         49

#define LLL_DIR_PIN          52
#define LLL_STEP_PIN         53

#define RUL_STEP_HIGH             PORTC |=  0b00000001;
#define RUL_STEP_LOW              PORTC &= ~0b00000001;

#define RML_STEP_HIGH             PORTG |=  0b00000001;
#define RML_STEP_LOW              PORTG &= ~0b00000001;

#define RLL_STEP_HIGH             PORTL |=  0b00010000;
#define RLL_STEP_LOW              PORTL &= ~0b00010000;

#define LUL_STEP_HIGH             PORTL |=  0b00000001;
#define LUL_STEP_LOW              PORTL &= ~0b00000001;

#define LLL_STEP_HIGH             PORTB |=  0b00000001;
#define LLL_STEP_LOW              PORTB &= ~0b00000001;



#define TIMER1_INTERRUPTS_ON    TIMSK1 |=  (1 << OCIE1A);
#define TIMER1_INTERRUPTS_OFF   TIMSK1 &= ~(1 << OCIE1A);

struct stepperInfo {
  // Lobe-specific parameters
  void (*dirFunc)(int);
  void (*stepFunc)();
  volatile int uml;                        // upper(0), middle(1), or lower(2) position
  volatile unsigned int default_steps = 100;
  volatile unsigned int default_delay = 2000;

  // derived parameters
  long stepPosition;              // current position of stepper (total of all movements taken so far)

  // per movement variables (only changed once per movement)
  volatile int dir;                        // current direction of movement, used to keep track of position
  volatile unsigned int totalSteps;        // number of steps requested for current movement
  volatile bool movementDone = false;      // true if the current movement has been completed (used by main program to wait for completion)

  // per iteration variables (potentially changed every interrupt)
  volatile float d;                        // current interval length
  volatile unsigned long di;               // above variable truncated
  volatile unsigned int stepCount;         // number of steps completed in current movement

};

void rulStep() {
  RUL_STEP_HIGH
delayMicroseconds(10);
  RUL_STEP_LOW
delayMicroseconds(10);
}
void rulDir(int dir) {
  dir = dir == LOW ? HIGH : LOW;
  digitalWrite(RUL_DIR_PIN, dir);
}

void rmlStep() {
  RML_STEP_HIGH
delayMicroseconds(10);
  RML_STEP_LOW
delayMicroseconds(10);
}
void rmlDir(int dir) {
  digitalWrite(RML_DIR_PIN, dir);
}

void rllStep() {
  RLL_STEP_HIGH
delayMicroseconds(10);
  RLL_STEP_LOW
delayMicroseconds(10);
}
void rllDir(int dir) {
  dir = dir == LOW ? HIGH : LOW;
  digitalWrite(RLL_DIR_PIN, dir);
}

void lulStep() {
  LUL_STEP_HIGH
delayMicroseconds(10);
  LUL_STEP_LOW
delayMicroseconds(10);
}
void lulDir(int dir) {
  digitalWrite(LUL_DIR_PIN, dir);
}

void lllStep() {
  LLL_STEP_HIGH
delayMicroseconds(10);
  LLL_STEP_LOW
delayMicroseconds(10);
}
void lllDir(int dir) {
  digitalWrite(LLL_DIR_PIN, dir);
}

void resetStepperInfo( stepperInfo& si ) {
  si.d = 0;
  si.di = 0;
  si.stepCount = 0;
  si.totalSteps = 0;
  si.stepPosition = 0;
  si.movementDone = false;
}

volatile stepperInfo steppers[NUM_STEPPERS];

void setup() {

  Serial.begin(19200);
  Serial.flush();
  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(RUL_STEP_PIN,   OUTPUT);
  pinMode(RUL_DIR_PIN,    OUTPUT);

  pinMode(RML_STEP_PIN,   OUTPUT);
  pinMode(RML_DIR_PIN,    OUTPUT);

  pinMode(RLL_STEP_PIN,   OUTPUT);
  pinMode(RLL_DIR_PIN,    OUTPUT);

  pinMode(LUL_STEP_PIN,   OUTPUT);
  pinMode(LUL_DIR_PIN,    OUTPUT);

  pinMode(LLL_STEP_PIN,   OUTPUT);
  pinMode(LLL_DIR_PIN,    OUTPUT);


  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1  = 0;

  OCR1A = 1000;                             // compare value
  TCCR1B |= (1 << WGM12);                   // CTC mode
  TCCR1B |= ((1 << CS11) | (1 << CS10));    // 64 prescaler
  interrupts();

  steppers[rul].dirFunc = rulDir;
  steppers[rul].stepFunc = rulStep;
  steppers[rul].uml = 0;

  steppers[rml].dirFunc = rmlDir;
  steppers[rml].stepFunc = rmlStep;
  steppers[rml].uml = 1;

  steppers[rll].dirFunc = rllDir;
  steppers[rll].stepFunc = rllStep;
  steppers[rll].uml = 2;

  steppers[lul].dirFunc = lulDir;
  steppers[lul].stepFunc = lulStep;
  steppers[lul].uml = 0;

  steppers[lll].dirFunc = lllDir;
  steppers[lll].stepFunc = lllStep;
  steppers[lll].uml = 2;
}

void resetStepper(volatile stepperInfo& si) {
  si.di = si.d;
  si.stepCount = 0;
  si.movementDone = false;
}

volatile byte remainingSteppersFlag = 0;

void prepareMovement(int whichMotor, int steps) {
  volatile stepperInfo& si = steppers[whichMotor];
  si.dirFunc( steps < 0 ? HIGH : LOW );
  si.dir = steps > 0 ? 1 : -1;
  si.totalSteps = abs(steps);
  resetStepper(si);
  remainingSteppersFlag |= (1 << whichMotor);
}

volatile byte nextStepperFlag = 0;

void setNextInterruptInterval() {

    // Serial.println(remainingSteppersFlag, BIN);

  unsigned int mind = 65535;
  for (int i = 0; i < NUM_STEPPERS; i++) {
    if ( ((1 << i) & remainingSteppersFlag) && steppers[i].di < mind ) {
      mind = steppers[i].di;
    }
  }

  nextStepperFlag = 0;
  for (int i = 0; i < NUM_STEPPERS; i++) {
    if ( ((1 << i) & remainingSteppersFlag) && steppers[i].di == mind )
      nextStepperFlag |= (1 << i);
  }

  OCR1A = mind;

  // Serial.print(F("OCR1A: "));
  // Serial.println(OCR1A);
}

ISR(TIMER1_COMPA_vect)
{
  // Serial.println(TCNT1);
  unsigned int tmpCtr = OCR1A;

  OCR1A = 65535;
  

  for (int i = 0; i < NUM_STEPPERS; i++) {

    if ( ! ((1 << i) & remainingSteppersFlag) )
      continue;

    if ( ! (nextStepperFlag & (1 << i)) ) {
      steppers[i].di -= tmpCtr;
      continue;
    }

    volatile stepperInfo& s = steppers[i];

    if ( s.stepCount < s.totalSteps ) {
      s.stepFunc();
      s.stepCount++;
      s.stepPosition += s.dir;
      // s.d = p[0][s.uml][s.stepCount];
      s.d = delays[i][s.stepCount];
      if ( s.stepCount >= s.totalSteps ) {
        s.movementDone = true;
        remainingSteppersFlag &= ~(1 << i);
      }
    }

    s.di = s.d; // Set integer delay
//    Serial.println(s.di);
//    Serial.println(s.stepCount);
  }
  setNextInterruptInterval();
  // Serial.println(TCNT1);
  TCNT1  = 0; // The timer continues to run during the ISR and movements. Set to 0 in case time is passed
}

void runAndWait() {
  // Serial.println("Begin run");
  noInterrupts();
  OCR1A = 65535;
  TCNT1 = 0;
  interrupts();
  setNextInterruptInterval();
  TIMER1_INTERRUPTS_ON
  while ( remainingSteppersFlag ); // Wait until motion is finished
  TIMER1_INTERRUPTS_OFF
//   setNextInterruptInterval();
}


//============
// Serial processing variables
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing
boolean newData = false;

// Mutable parameters
float DELAY_PROFILE = 0.1;
int PROFILE_CYCLES = 5;
float DELAY_INHALE = 0.1;
float DELAY_EXHALE = 0.1;
int START_MANEUVER = exhale;



void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
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

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

#define SEP "/"

void checkType() {
    // Serial.print(F("tempChars: "));
    // Serial.println(tempChars);
    switch (tempChars[0])
    {
    case '?':
        parseQuery();
        break;
    case 'S':
        parseS();
        break;
    case 'R':
        if (strcmp(tempChars, "RUN") == 0)
        {
            // runAndWait();
            // if (!RUN) {
            //     RUN = true;
            // } else {
            //     RUN = false;
            // }
            runAndWait();
        } else
        {
            printInvalid();
        }
        break;
    case 'P':
        if (strcmp(tempChars, "PROFILEC") == 0)
        {
            run_profile_constant();
        } else if (strcmp(tempChars, "PROFILEV") == 0) {
            run_profile_variable();
        } else
        {
            printInvalid();
        }
        break;
    case 'C':
        parseC();
        break;
    default:
        printInvalid();
        break;
    }
}

void parseQuery() {
    // if (strcmp(tempChars, "?") == 0)
    // {
    //     Serial.println(F("OK"));
    // }
    if (true)
    {
      switch (tempChars[1]) {
        case '\0':
          Serial.println("OK");
          break;
        case 'S':
        printParams();
        break;
        case 'A':
        printDelays();
        break;
        default:
        printInvalid();
        break;
      }
    }
}

void parseS() {
    // Input: S{Setting}/{Value}/{Additional parameters}

    char * strtokIndx;

    char setting[10];
    float val = 0;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atof(strtokIndx); 

    switch (setting[1])
    {
    case 'A':
      switch (setting[2]) {
        case 'I':
            parseSAI();
            break;
        case 'C':
            parseSAC();
            break;
      }
      break;
    case 'D':
        switch (setting[2])
        {
        case 'I':
            DELAY_INHALE = val;
            break;
        case 'E':
            DELAY_EXHALE = val;
            break;
        case 'P':
            DELAY_PROFILE = val;
            break;
        }
        break;
    case 'L':
        parseSL();
        break;
    case 'M':
        parseSM();
        break;
    case 'N':
        // Set the number of breathing cycles
        PROFILE_CYCLES = val;
        break;
    case 'O':
        switch (setting[2])
        {
        case 'I':
            START_MANEUVER = inhale;
            break;
        case 'E':
            START_MANEUVER = exhale;
            break;
        }
        break;
    default:
        printInvalid();
        return;
    }
}

void parseSL() {
  // Input: SL{Setting}/{Value}/{Additional parameters}
  // Set lobe-specific parameters

  strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    char motors[5];
    unsigned int val = 0;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx); 

    switch (setting[2])
    {
    case 'S':
        // Set steps
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                steppers[i].default_steps = val;
            }
            else
            {
                Serial.print(i);
                Serial.print(F(": "));
                Serial.println(F("Not set"));
            }
            
        }
        break;

    case 'D':
        // Set delays
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                steppers[i].default_delay = val;
            }
            else
            {
                Serial.print(i);
                Serial.print(F(": "));
                Serial.println(F("Not set"));
            }
            
        }
        break;
    
    default:
        printInvalid();
        return;
    }

}

void parseSM() {
    // Input: SM{Maneuver}/{Steps}/{Motors}

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    char motors[5];
    int val = 0;
    int maneuver;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx); 

    switch (setting[2])
    {
    case 'I':
        maneuver = inhale;
        break;

    case 'E':
        maneuver = exhale;
        break;
    
    default:
        printInvalid();
        return;
    }

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            prepareM(i, maneuver*val);
        }
        else
        {
            Serial.print(i);
            Serial.print(F(": "));
            Serial.println(F("Not set"));
        }
        
    }

}

void parseSAI() {
    // Write
    // Input: SAI/{Index}/{Value}/{Motors}
    // Index: 0 - 500
    // Value: 0 - 65535
    // Motors: xxxxx

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    unsigned int index = 0;
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    index = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    // Serial.print("Setting: ");
    // Serial.println(setting);

    // Serial.print("Index: ");
    // Serial.println(index);

    // Serial.print("Value: ");
    // Serial.println(val);

    // Serial.print("Motors: ");
    // Serial.println(motors);

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            delays[i][index] = val;
        }
        
    }
    
    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            if (delays[i][index] == val) {
                Serial.println("OK");
            } else {
                Serial.println("Error");
            }
        }
        
    }

}

void parseSAC() {
    // Write
    // Input: SAC/{Value}/{Motors}
    // Value: 0 - 65535
    // Motors: xxxxx

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    if (val == 0 && motors[0] == '\0')
    // Use default values for all lobes
    {
        for (size_t i = 0; i < 5; i++)
        {
            for (size_t j = 0; j < 500; j++)
            {
                delays[i][j] = steppers[i].default_delay;
            }
        }
    }
    else
    {
      // Use specified value for given lobes
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                for (size_t j = 0; j < 500; j++)
                {
                    delays[i][j] = val;
                }
            }
        }
    }
}

void parseC() {
    // Write
    // Input: C{Maneuver}/{Steps}/{Value}/{Motors}
    // Index: 0 - 500
    // Value: 0 - 65535
    // Motors: xxxxx

    char * strtokIndx;

    char setting[15];
    unsigned int index = 0;
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    index = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    // Serial.print("Setting: ");
    // Serial.println(setting);

    // Serial.print("Index: ");
    // Serial.println(index);

    // Serial.print("Value: ");
    // Serial.println(val);

    // Serial.print("Motors: ");
    // Serial.println(motors);

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
          for (size_t j = 0; j < index; j++)
          {
            delays[i][j] = val;
          }
        }
        
    }

    Serial.println("OK");
    
}

void prepareM(int i, int steps) {
    Serial.print(i);
    Serial.print(F(": "));
    Serial.print(steps);
    Serial.println(" steps");
    prepareMovement(i, steps);
}

void prepare_delays_constant() {
    // Set delays to default for each motor
    for (size_t i = 0; i < 5; i++)
        {
            for (size_t j = 0; j < 500; j++)
            {
                delays[i][j] = steppers[i].default_delay;
            }
        }
}

void run_profile_constant() {
prepare_delays_constant();
    delay(DELAY_PROFILE * 1000);

    for (int n = 0; n < PROFILE_CYCLES; n++)
    {
        // First breath maneuver
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * steppers[i].default_steps);
        }
        delay(DELAY_INHALE * 1000);
        runAndWait();

        // Second breath maneuver
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * -1 * steppers[i].default_steps);
        }
        delay(DELAY_EXHALE * 1000);
        runAndWait();
    }
}

    // Example of reading from progmem
    // unsigned int displayInt;
    // displayInt = pgm_read_word_near(&(stored_inhale[whichMotor][k]));
    // delays[whichMotor][k] = displayInt;
    // Serial.print(displayInt);
    // Serial.print(',');

void prepare_delays_variable(int maneuver) {
    if (maneuver == inhale) {
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            for (int k = 0; k < 500; k++) {
                delays[whichMotor][k] = pgm_read_word_near(&(stored_inhale[whichMotor][k]));
            }
        }
    } else {
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            for (int k = 0; k < 500; k++) {
                delays[whichMotor][k] = pgm_read_word_near(&(stored_exhale[whichMotor][k]));
            }
        }
    }
}

void run_profile_variable() {
    // Delay profile time
    delay(DELAY_PROFILE * 1000);
    // for number of breath cycles
    for (int n = 0; n < PROFILE_CYCLES; n++) {
        // Prepare first movement delays
        prepare_delays_variable(START_MANEUVER);

        // Prepare first movement
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * steppers[i].default_steps);
        }
        // First movement (inhale) delay period
        delay(DELAY_INHALE * 1000);
        runAndWait();

        // Prepare second movement delays
        prepare_delays_variable(START_MANEUVER*-1);
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * -1 * steppers[i].default_steps);
        }
        // Second movement delay period
        delay(DELAY_EXHALE * 1000);
        runAndWait();
    }
}

void printInvalid() {
    Serial.println(F("Invalid command"));
}

void printDelays() {
    Serial.println(F("Current delays:"));
  for (size_t i = 0; i < 5; i++)
        {
          Serial.print(F("Lobe "));
          Serial.print(i);
          Serial.print(F(": {"));
            for (size_t j = 0; j < 500; j++)
            {
                Serial.print(delays[i][j]);
                Serial.print(F(","));
            }
            Serial.println("}");
        }
        Serial.println(F("Stored inhale delays:"));
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            Serial.print(F("Lobe "));
            Serial.print(whichMotor);
            Serial.print(F(": {"));
            for (int k = 0; k < 500; k++) {
                Serial.print(pgm_read_word_near(&(stored_inhale[whichMotor][k])));
                Serial.print(F(","));
            }
            Serial.println("}");
        }
        Serial.println(F("Stored exhale delays:"));
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            Serial.print(F("Lobe "));
            Serial.print(whichMotor);
            Serial.print(F(": {"));
            for (int k = 0; k < 500; k++) {
                Serial.print(pgm_read_word_near(&(stored_exhale[whichMotor][k])));
                Serial.print(F(","));
            }
            Serial.println("}");
        }
}

void printParams() {
    Serial.print(F("Delay profile (s): "));
    Serial.println(DELAY_PROFILE);

    Serial.print(F("Profile cycles: "));
    Serial.println(PROFILE_CYCLES);

    for (size_t i = 0; i < 5; i++)
    {
        Serial.print(F("Motor "));
        Serial.print(i);
        Serial.print(F(": "));
        Serial.print(steppers[i].default_steps);
        Serial.println(" steps");

        Serial.print(F("Motor "));
        Serial.print(i);
        Serial.print(F(": "));
        Serial.print(steppers[i].default_delay);
        Serial.println(" delay");

        Serial.print("Motor ");
        Serial.print(i);
        Serial.print(" position: ");
        Serial.println(steppers[i].stepPosition);
    }

    Serial.print(F("Delay inhale (s): "));
    Serial.println(DELAY_INHALE);

    Serial.print(F("Delay exhale (s): "));
    Serial.println(DELAY_EXHALE);

    Serial.print(F("Start maneuver: "));
    Serial.println(START_MANEUVER);
}



void loop() {

    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        checkType();
        newData = false;
        // Serial.print(F("remainingSteppersFlag: "));
        // Serial.println(remainingSteppersFlag, BIN);
    }

}
