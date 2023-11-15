import os
import serial
from time import sleep
from datetime import datetime
import pandas as pd

class TSI:

    def __init__(self, port):
        self.dev = serial.Serial(
            port,
            baudrate = 38400,
            bytesize = serial.EIGHTBITS,
            xonxoff = False,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            timeout = 0.5,
            rtscts = False,
            dsrdtr = False
        )

        sleep(1)

        self.set_output_dir(os.path.join(os.path.dirname(__file__), r"output"))
        



    ###
    # Communications
    ###

    def read(self):
        line = self.dev.readline().decode('ascii').strip()
        return line

    def query_connection(self, message = "?\r"):
        self.dev.write(message.encode('ascii'))
        lines = self.dev.readlines()
        for index, line in enumerate(lines):
            lines[index] = line.decode('ascii').strip()
        return lines
    
    def query_flow_set(self):
        self.dev.write('DBFxx1000\r'.encode('ascii'))
        if self.dev.read(1) == b'\x00':
            byte = b''
            while not byte:
                # do nothing
                byte = self.dev.read(1)

            results = self.convert(byte)
            self.save_flow_set(results)

    def query_volume(self):
        # Query volume data
        self.dev.write('VB1000\r'.encode('ascii'))

        if self.dev.read(1) == b'\x00':
            byte = b''
            while not byte:
                # do nothing
                byte = self.dev.read(1)

            results = self.convert_volume(byte)

    ### 
    # Data processing
    ###

    def convert(self, byte = None):
        f = []
        results = bytearray()

        if not byte:
            byte = self.dev.read(1)      
        
        data = byte+self.dev.read(1)

        results += data

        while data and data != b'\xff\xff':
            # Parse binary and add to the appropriate list
            f.append(int.from_bytes(data[0:2], 'big', signed=False)/100)
            # For when temp and pressure may be read later
            # t.append(int.from_bytes(data[2:4], 'big', signed=True)/100)
            # p.append(int.from_bytes(data[4:6], 'big', signed=False)/100)
            
            data = self.dev.read(2)
            results += data
        
        return f

    def convert_volume(self, byte = None):
        results = bytearray()

        if not byte:
            byte = self.dev.read(1)      
        
        data = byte+self.dev.read(1)

        results += data

        print(f"V: {int.from_bytes(data[0:2], 'big', signed=False)/100}")
        return results

    ###
    # Data export
    ###

    def set_output_dir(self, dir):
        if (not os.path.exists(dir)):
            os.mkdir(dir)
        self.outdir = dir

    def save_flow_set(self, data):
        # Save data - max readable at one time is 1000 points

        filetime = datetime.now().strftime("%y%m%d-%H%M%S")
        file_path = os.path.join(self.outdir,f'data-{filetime}.csv')

        df = pd.DataFrame(data)
        df.to_csv(file_path)

class TSI_Win:

    def __init__(self, port):
        self.port = port
        self.set_output_dir(os.path.join(os.path.dirname(__file__), r"output"))
        

        sleep(1)

    ###
    # Communications
    ###

    def establish_connection(self):
        self.dev = serial.Serial(
            self.port,
            baudrate = 38400,
            bytesize = serial.EIGHTBITS,
            xonxoff = False,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            timeout = 0.5,
            rtscts = False,
            dsrdtr = False
        )

    def read(self):
        line = self.dev.readline().decode('ascii').strip()
        return line

    def query_connection(self, message = "?\r"):
        self.dev.write(message.encode('ascii'))
        lines = self.dev.readlines()
        for index, line in enumerate(lines):
            lines[index] = line.decode('ascii').strip()
        return lines
    
    def query_flow_set(self):
        self.dev.write('DBFxx1000\r'.encode('ascii'))
        if self.dev.read(1) == b'\x00':
            byte = b''
            while not byte:
                # do nothing
                byte = self.dev.read(1)

            results = self.convert(byte)
            self.save_flow_set(results)

    def query_volume(self):
        # Query volume data
        self.dev.write('VB1000\r'.encode('ascii'))

        if self.dev.read(1) == b'\x00':
            byte = b''
            while not byte:
                # do nothing
                byte = self.dev.read(1)

            results = self.convert_volume(byte)

    ### 
    # Data processing
    ###

    def convert(self, byte = None):
        f = []
        results = bytearray()

        if not byte:
            byte = self.dev.read(1)      
        
        data = byte+self.dev.read(1)

        results += data

        while data and data != b'\xff\xff':
            # Parse binary and add to the appropriate list
            f.append(int.from_bytes(data[0:2], 'big', signed=False)/100)
            # For when temp and pressure may be read later
            # t.append(int.from_bytes(data[2:4], 'big', signed=True)/100)
            # p.append(int.from_bytes(data[4:6], 'big', signed=False)/100)
            
            data = self.dev.read(2)
            results += data
        
        return f

    def convert_volume(self, byte = None):
        results = bytearray()

        if not byte:
            byte = self.dev.read(1)      
        
        data = byte+self.dev.read(1)

        results += data

        print(f"V: {int.from_bytes(data[0:2], 'big', signed=False)/100}")
        return results

    ###
    # Data export
    ###

    def set_output_dir(self, dir):
        if (not os.path.exists(dir)):
            os.mkdir(dir)
        self.outdir = dir

    def save_flow_set(self, data):
        # Save data - max readable at one time is 1000 points

        filetime = datetime.now().strftime("%y%m%d-%H%M%S")
        file_path = os.path.join(self.outdir,f'data-{filetime}.csv')

        df = pd.DataFrame(data)
        df.to_csv(file_path)