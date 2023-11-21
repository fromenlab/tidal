import serial
from time import sleep
from datetime import datetime
import os

# Lobes always specified in the order RU, RM, RL, LU, LL

class Arduino:
    def __init__(self, port):
        self.port = port

    def connect(self, port = None, baudrate = 19200):
        # Change the port if specified manually
        if port is not None:
            self.port = port

        try:
            self.dev = serial.Serial(self.port, baudrate, timeout = 0.5)
            sleep(1)
        except serial.SerialException as e:
            print(f"There was an error connecting: {e}")
        else:
            print(f"Connected to Arduino on port {self.port}")

    def close(self):
        try:
            self.dev.close()
        except:
            print(f"There was an error disconnecting on port {self.port}")
        else:
            print(f"Disconnected from {self.port}")

    def format(self, fragments):
        if (type(fragments) is list):
            message = ('/').join([str(_) for _ in fragments])
        else:
            message = str(fragments)
        return f"<{message}>"

    def query(self, message):
        message = self.format(message)
        print(f"Sending: {message}")
        self.dev.write(message.encode('ascii'))
        lines = [_.decode('ascii').strip() for _ in self.dev.readlines()]
        return lines

    def check_connection(self):
        return self.query('?')

    def check_parameters(self):
        return self.query('?S')
    
    def check_lobe_delays(self):
        return self.query('?A')

    # Setters

    ## Global Settings

    def set_breath_count(self, n):
        self.query(['SN', n])

    ### Delays are specified in seconds

    def set_delay(self, maneuver, delay):
        maneuver_char = ''
        
        if (maneuver == 'profile'):
            maneuver_char = 'P'
        elif (maneuver == 'inhale'):
            maneuver_char = 'I'
        elif (maneuver == 'exhale'):
            maneuver_char = 'E'
        
        return self.query([f"SD{maneuver_char}", delay])

    def set_maneuver_order(self, maneuver):
        maneuver_char = ''
        
        if (maneuver == 'inhale'):
            maneuver_char = 'I'
        elif (maneuver == 'exhale'):
            maneuver_char = 'E'
        
        return self.query(f"SO{maneuver_char}")
    
    ## Lobe settings

    def set_lobe_default(self, parameter, value, motors):
        if parameter == 'steps':
            self.query(['SLS', value, motors])
        elif parameter == 'delay':
            self.query(['SLD', value, motors])

    def update_lobe_delays(self, value = None, motors = None):
        if not (value and motors):
            self.query(['SAC'])

    # Maneuvers

    def prepare_maneuver(self, maneuver, steps, motors):
        maneuver_char = ''
        
        if (maneuver == 'inhale'):
            maneuver_char = 'I'
        elif (maneuver == 'exhale'):
            maneuver_char = 'E'

        return self.query([f"SM{maneuver_char}", steps, motors])

    def run_maneuver(self):
        return self.query('RUN')

    def run_profile_constant(self):
        # Set breathing parameters before running profile
        return self.query('PROFILEC')
    
    def run_profile_variable(self):
        # Set breathing parameters before running profile
        return self.query('PROFILEV')