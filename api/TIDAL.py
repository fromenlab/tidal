from api.arduino_motor import Arduino
from api.tsi import TSI
import os
from utils.logger import Logger

class TIDAL():
    def __init__(self, tsi_port = None, motor_port = None) -> None:
        # Lobes
        #   - Delays
        #       - Inhale
        #       - Exhale
        #   - Control points
        #       - Inhale
        #       - Exhale
        self.tsi = None
        self.tsi_connected = False
        self.arduino = None
        self.log_dir = os.path.join(os.path.dirname(__file__), r"logs")
        self.logger = None

        self.init_lobes()
        self.init_lobe_entries()
        self.init_global_entries()

        if motor_port:
            self.set_motor_port(motor_port)
            # self.connect_motors()

        if tsi_port:
            self.set_tsi_port(tsi_port)
            # self.connect_tsi()

        pass

    # 
    # Connections
    # 

    def set_tsi_port(self, port):
        self.tsi_port = port
        self.tsi = TSI(self.tsi_port)

    def get_tsi_port(self):
        return self.tsi_port

    def connect_tsi(self):
        # Connect to flow meter
        if self.tsi is None:
            self.tsi = TSI(self.get_tsi_port())
            self.tsi.connect(self.get_tsi_port())
        else:
            self.tsi.connect(self.get_tsi_port())
        self.tsi_connected = True

    def get_tsi(self):
        return self.tsi

    def disconnect_tsi(self):
        # Disconnect flow meter
        self.tsi.close()
        self.tsi_connected = False

    def set_motor_port(self, port):
        self.motor_port = port

    def get_motor_port(self):
        return self.motor_port

    def connect_motors(self):
        # Connect to Arduino
        self.arduino = Arduino(self.get_motor_port())
        self.motors_connected = True

    def get_motors(self):
        return self.arduino

    def disconnect_motors(self):
        # Disconnect from Arduino
        self.arduino.close()
        self.motors_connected = False

    # 
    # Logging
    # 


    # The log dir is where information on each run will be recorded
    def set_log_dir(self, dir):
        self.log_dir = dir

    def get_log_dir(self):
        return self.log_dir
    
    # The run ID is a ~unique identifier for each set of experimental conditions
    def set_run_id(self, id):
        self.run_id = id

    def get_run_id(self):
        return self.run_id

    # The run dir is where information on each set of experimental conditions and associated data will be recorded
    def set_run_dir(self, dir):
        self.run_dir = dir
        if self.logger:
            self.logger.set_file_output(os.path.join(dir, "log.txt"))

    def get_run_dir(self):
        return self.run_dir
    
    # The data dir is where measured output from each run will be recorded
    def set_data_dir(self, dir):
        self.data_dir = dir

    def get_data_dir(self):
        return self.data_dir
    
    def set_logger(self, logger: Logger):
        self.logger = logger

    def get_logger(self):
        return self.logger
    

    # 
    # Maneuver panel
    # 
    def init_lobes(self):
        self.lobes = {
            'RU': 0,
            'RM': 0,
            'RL': 0,
            'LU': 0,
            'LL': 0
        }

    def init_lobe_entries(self):
        self.lobe_entries = {
            'RU': {
                'steps': None,
                'delay': None
            },
            'RM': {
                'steps': None,
                'delay': None
            },
            'RL': {
                'steps': None,
                'delay': None
            },
            'LU': {
                'steps': None,
                'delay': None
            },
            'LL': {
                'steps': None,
                'delay': None
            }
        }

    def init_global_entries(self):
        self.global_entries = {
            "Breath count": None, 
            "Profile delay (s)": None, 
            "Inhale delay (s)": None, 
            "Exhale delay (s)": None,
            }
        self.order = None