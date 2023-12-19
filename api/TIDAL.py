from api.arduino_motor import Arduino
from api.tsi import TSI
import os
from utils.logger import Logger
from api.lobe import Lobe
from api.bezier import Bezier

import json
from string import Template
import subprocess

class TIDAL():
    def __init__(self, tsi_port = None, motor_port = None) -> None:
        self.tsi = None
        self.tsi_connected = False
        self.arduino = None
        self.motors_connected = False

        self.log_dir = r'./logs'
        self.run_dir = os.path.join(self.log_dir, "runs")
        self.data_dir = os.path.join(self.run_dir, "data")
        self.log_file = os.path.join(self.run_dir, "log.txt")
        self._logger = None

        # Property values
        self.breath_count = None
        self.profile_delay_s = None
        self.inhale_delay_s = None
        self.exhale_delay_s = None
        self.order = None
        self.lobes = [Lobe(name) for name in ['RU', 'RM', 'RL', 'LU', 'LL']]
        
        # GUI-related
        self.global_entries = {
            "Breath count": None, 
            "Profile delay (s)": None, 
            "Delay inhale (s)": None, 
            "Delay exhale (s)": None,
            }
        self.order_entry = None
        

        if motor_port:
            self.set_motor_port(motor_port)
            self.arduino = Arduino(motor_port)

        if tsi_port:
            self.set_tsi_port(tsi_port)
            self.tsi = TSI(tsi_port)
            

        return
        

    # 
    # Import/Export configurations
    # 

    def load(self):
        from tkinter import filedialog
        try:
            with filedialog.askopenfile(defaultextension=".tidal", filetypes=[('TIDAL','*.tidal'), ('All files', '*.*')]) as f:
                tidal_config = json.load(f)
                # Update TIDAL instance
                self.breath_count = tidal_config['Breath count']
                self.profile_delay_s = tidal_config['Profile delay (s)']
                self.inhale_delay_s = tidal_config['Delay inhale (s)']
                self.exhale_delay_s = tidal_config['Delay exhale (s)']
                self.order = tidal_config['order']
                for lobe in self.lobes:
                    for config in tidal_config['lobes']:
                        if lobe.name == config['name']:
                            lobe.inhale_control_points = config['inhale_control_points']
                            lobe.exhale_control_points = config['exhale_control_points']
                            lobe.step_count_constant = config['step_count_constant']
                            lobe.step_delay_constant = config['step_delay_constant']
                            lobe.step_count_variable = config['step_count_variable']
                            lobe.imin = config['imin']
                            lobe.imax = config['imax']
                            lobe.emin = config['emin']
                            lobe.emax = config['emax']

                # Set GUI based on TIDAL instance
                self.global_entries['Breath count'].delete(0, 'end')
                self.global_entries['Breath count'].insert(0, self.breath_count)
                self.global_entries['Profile delay (s)'].delete(0, 'end')
                self.global_entries['Profile delay (s)'].insert(0, self.profile_delay_s)
                self.global_entries['Delay inhale (s)'].delete(0, 'end')
                self.global_entries['Delay inhale (s)'].insert(0, self.inhale_delay_s)
                self.global_entries['Delay exhale (s)'].delete(0, 'end')
                self.global_entries['Delay exhale (s)'].insert(0, self.exhale_delay_s)
                self.order_entry.current(self.order)

                for lobe in self.lobes:
                    for config in tidal_config['lobes']:
                        if lobe.name == config['name']:
                            lobe.gui_constant_step_entry.delete(0, 'end')
                            lobe.gui_constant_step_entry.insert(0, lobe.step_count_constant)
                            lobe.gui_constant_delay_entry.delete(0, 'end')
                            lobe.gui_constant_delay_entry.insert(0, lobe.step_delay_constant)

                            lobe.gui_variable_step_entry.delete(0, 'end')
                            lobe.gui_variable_step_entry.insert(0, lobe.step_count_variable)

                            lobe.gui_variable_inhale_min_delay_entry.delete(0, 'end')
                            lobe.gui_variable_inhale_min_delay_entry.insert(0, lobe.imin)
                            lobe.gui_variable_inhale_max_delay_entry.delete(0, 'end')
                            lobe.gui_variable_inhale_max_delay_entry.insert(0, lobe.imax)
                            lobe.gui_variable_exhale_min_delay_entry.delete(0, 'end')
                            lobe.gui_variable_exhale_min_delay_entry.insert(0, lobe.emin)
                            lobe.gui_variable_exhale_max_delay_entry.delete(0, 'end')
                            lobe.gui_variable_exhale_max_delay_entry.insert(0, lobe.emax)

                            lobe.gui_inhale_bezier.interactor.control_x = lobe.inhale_control_points['x']
                            lobe.gui_inhale_bezier.interactor.control_y = lobe.inhale_control_points['y']
                            lobe.gui_exhale_bezier.interactor.control_x = lobe.exhale_control_points['x']
                            lobe.gui_exhale_bezier.interactor.control_y = lobe.exhale_control_points['y']

                            lobe.gui_inhale_bezier.interactor.update_bezier()
                            lobe.gui_exhale_bezier.interactor.update_bezier()

        except Exception as e:
            print(f"There was an error in loading the configuration: {e}")
        else: 
            print(f"Configuration loaded from: {f.name}")

        # self.disconnect_motors()
        # self.disconnect_tsi()

    def save(self, filename = None):
        from tkinter import filedialog
        # Update parameters
        self.breath_count =  self.global_entries['Breath count'].get()
        self.profile_delay_s = self.global_entries['Profile delay (s)'].get()
        self.inhale_delay_s = self.global_entries['Delay inhale (s)'].get()
        self.exhale_delay_s = self.global_entries['Delay exhale (s)'].get()
        self.order = self.order_entry.current()
        for lobe in self.lobes: lobe.update_variable_profile_params()

        # Write file
        try:
            if filename is None:
                with filedialog.asksaveasfile(defaultextension=".tidal", filetypes=[('TIDAL','*.tidal'), ('All files', '*.*')]) as f:
                    json.dump(self, f, indent = 4, cls = TIDALEncoder)
            else:
                with open(os.path.join(self.run_dir, filename), 'w') as f:
                    json.dump(self, f, indent = 4, cls = TIDALEncoder)
        except Exception as e:
            print(f"There was an error in saving the configuration: {e}")
        else: 
            print(f"Configuration saved at: {f.name}")

    # 
    # Connections
    # 

    ##########
    # Flow meter
    ##########

    def set_tsi_port(self, port):
        self.tsi_port = port

        # Instantiate TSI if a port was not supplied on initial setup
        if self.tsi is None:
            self.tsi = TSI(port)
        else:
            self.tsi.port = port

    def get_tsi_port(self):
        return self.tsi_port
    
    def get_tsi(self):
        return self.tsi

    def connect_tsi(self):
        if (self.tsi and self.tsi_port):
            # Connect to flow meter
            try:
                self.tsi.connect()
            except:
                print(f"TIDAL could not connect to flow meter")
            else:
                self.tsi_connected = True
        else:
            print(f"There was no existing TSI or port specified")

    def disconnect_tsi(self):
        # Disconnect flow meter
        try:
            self.tsi.close()
        except:
            print(f"TIDAL could not disconnect from flow meter")
        else:
            self.tsi_connected = False

    ##########
    # Arduino
    ##########

    def set_motor_port(self, port):
        self.motor_port = port

        # Instantiate Arduino if a port was not supplied on initial setup
        if self.arduino is None:
            self.arduino = Arduino(port)
        else:
            self.arduino.port = port

    def get_motor_port(self):
        return self.motor_port
    
    def get_motors(self):
        return self.arduino

    def connect_motors(self):
        if (self.arduino and self.motor_port):
            # Connect to Arduino
            try:
                self.arduino.connect()
            except:
                print(f"TIDAL could not connect to motors")
            else:
                self.motors_connected = True
        else:
            print(f"There was no existing Arduino or port specified")

    def disconnect_motors(self):
        # Disconnect from Arduino
        try:
            self.arduino.close()
        except:
            print(f"TIDAL could not disconnect from motors")
        else:
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
        self.data_dir = os.path.join(self.run_dir, "data")
        self.log_file = os.path.join(self.run_dir, "log.txt")
        if self.logger:
            self.logger.set_file_output(self.log_file)

    def get_run_dir(self):
        return self.run_dir
    
    # The data dir is where measured output from each run will be recorded
    def set_data_dir(self, dir):
        self.data_dir = dir

    def get_data_dir(self):
        return self.data_dir

    @property
    def logger(self):
        return self._logger
    
    @logger.setter
    def logger(self, logger: Logger):
        self._logger = logger
    
    #
    # Variable profiles
    # 
    def update_variable_profile(self):
        self.substitute_params()
        try:
            self.push_arduino()
        except Exception as e:
            print(f"{e}")
        else:
            print("Arduino updated")
            self.connect_motors()
        return

    def substitute_params(self):
        with open(r'./protocol/template/motor_complete_profile.ino', "r") as t:
            template = Template(t.read())
            
        # Hard-coding values for now
        final_output = template.substitute(
            sub_inhale_ru = self.lobes[0].inhale_delays_formatted,
            sub_inhale_rm = self.lobes[1].inhale_delays_formatted,
            sub_inhale_rl = self.lobes[2].inhale_delays_formatted,
            sub_inhale_lu = self.lobes[3].inhale_delays_formatted,
            sub_inhale_ll = self.lobes[4].inhale_delays_formatted,

            sub_exhale_ru = self.lobes[0].exhale_delays_formatted,
            sub_exhale_rm = self.lobes[1].exhale_delays_formatted,
            sub_exhale_rl = self.lobes[2].exhale_delays_formatted,
            sub_exhale_lu = self.lobes[3].exhale_delays_formatted,
            sub_exhale_ll = self.lobes[4].exhale_delays_formatted
        )

        with open(r'./protocol/motor_complete_profile/motor_complete_profile.ino', "w") as output:
            output.write(final_output)

    def push_arduino(self):
        # Note: for success, the arduino-cli executable 
        # needs to be in the PATH environment variable

        # However, the appropriate version needs to be called for the given OS
        arduino_cli = 'arduino-cli' if os.name == "nt" else 'arduino-cli.app'

        # Disconnect motors
        if self.motors_connected:
            self.disconnect_motors()

        board = 'arduino:avr:mega'
        sketch = 'protocol/motor_complete_profile'
        port = self.motor_port

        # Compile
        # arduino-cli compile --fqbn arduino:avr:mega protocol/motor_complete

        cmd_verify = [arduino_cli, 'compile', '--fqbn', board, sketch]
        # subprocess.run(cmd_verify)

        # Upload
        # arduino-cli upload -p COM3 --fqbn arduino:avr:mega protocol/motor_complete

        cmd_upload = [arduino_cli, 'upload', '-p', port, '--fqbn', board, sketch, '--verbose', '--verify']
        # subprocess.run(cmd_upload)

        if (not os.path.exists(self.run_dir)):
            os.makedirs(self.run_dir)
        arduino_log_path = os.path.join(self.run_dir, 'arduino.log')

        with subprocess.Popen(cmd_verify, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            lines = proc.stdout.readlines()

            with open(arduino_log_path, "a", encoding="utf-8") as f:
                for line in lines:
                    text = line.decode('ascii')#.rstrip("\n")
                    f.writelines(text)

        with subprocess.Popen(cmd_upload, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            lines = proc.stdout.readlines()

            with open(arduino_log_path, "a", encoding="utf-8") as f:
                for line in lines:
                    text = line.decode('ascii')#.rstrip("\n")
                    f.writelines(text)

class TIDALEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Lobe):
            rep = {
                'name': obj.name,
                'step_count_constant': obj.step_count_constant,
                'step_delay_constant': obj.step_delay_constant,
                'step_count_variable': obj.step_count_variable,
                'imin': obj.imin,
                'imax': obj.imax,
                'emin': obj.emin,
                'emax': obj.emax,
                'inhale_control_points': obj.inhale_control_points,
                'exhale_control_points': obj.exhale_control_points
            }
            return rep
        elif isinstance(obj, TIDAL):
            rep = {}
            for setting in obj.global_entries:
                rep[setting] = obj.global_entries[setting].get()
            rep['order'] = obj.order
            rep['lobes'] = obj.lobes
            return rep
        return super().default(self, obj)