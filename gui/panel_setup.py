import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime

from api.tsi import TSI
from utils.logger import write_log
import utils.unique_id as utils
from api.TIDAL import TIDAL
from utils.version import get_software_version

class SetupPanel:
    def __init__(self, parent, tidal_instance: TIDAL = None):
        self.parent = parent
        self.tidal = tidal_instance
        # self.tsi = tidal_instance.get_tsi()
        self.log_process = None
        self.output_path = None     # Folder for all logs
        self.run_folder = None      # Folder for given log
        self.conditions = {
            "Device ID": None, 
            "Alignment": None, 
            "Temperature (C)": None, 
            "Relative Humidity (%)": None
            }

        fr = tk.Frame(self.parent)
        fr.grid(sticky=tk.NSEW)
        fr.columnconfigure(0,weight=1)

        self.make_config_entry(fr)
        self.make_log_entry(fr)
        self.make_tsi_entry(fr)
        self.make_arduino_entry(fr)
        self.make_run_entry(fr)

    def make_config_entry(self, parent):
        frame_config = ttk.Labelframe(parent, text = 'Configuration')
        button_load = tk.Button(frame_config, text = 'Load', command = lambda:self.tidal.load())
        button_save = tk.Button(frame_config, text = 'Save', command = lambda:self.tidal.save())

        button_load.pack(side = tk.LEFT, padx=5, expand = True, fill = tk.X, pady=5)
        button_save.pack(side = tk.LEFT, padx=5, expand = True, fill = tk.X, pady=5)
        frame_config.grid(sticky=tk.EW)

    def make_log_entry(self, parent):
        # Set frames for layout
        frame_paths = ttk.Labelframe(parent, text='Log Folder')
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(index=0, weight=1)

        entry_input = tk.Entry(frame_paths)
        try:
            entry_input.insert(0, self.tidal.get_log_dir())
        except:
            pass
        button_input = tk.Button(frame_paths, text = 'Select', command = lambda:self.select_folder(entry_input))
        
        button_input.grid(row = 1, column = 0, padx=5, pady=5, sticky=tk.EW)
        entry_input.grid(row=0, column=0, padx = 5, pady=5, sticky=tk.EW)

        return entry_input
    
    def make_tsi_entry(self, parent):
        # Set frames for layout
        frame_paths = ttk.Labelframe(parent, text='TSI Port')
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(index=0, weight=1)

        entry_input = tk.Entry(frame_paths)
        try:
            entry_input.insert(0, self.tidal.get_tsi_port())
        except:
            pass
        button_input = tk.Button(frame_paths, text = 'Connect')
        button_input.configure(command = lambda:self.connect_tsi(entry_input, button_input))
        
        button_input.grid(row = 1, column = 0, padx=5, pady=5, sticky=tk.EW)
        entry_input.grid(row=0, column=0, padx = 5, pady=5, sticky=tk.EW)

        return entry_input
    
    def make_arduino_entry(self, parent):
        # Set frames for layout
        frame_paths = ttk.Labelframe(parent, text='Arduino Port')
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(index=0, weight=1)

        entry_input = tk.Entry(frame_paths)
        try:
            entry_input.insert(0, self.tidal.get_motor_port())
        except:
            pass
        button_input = tk.Button(frame_paths, text = 'Connect')
        button_input.configure(command = lambda:self.connect_arduino(entry_input, button_input))
        
        button_input.grid(row = 1, column = 0, padx=5, pady=5, sticky=tk.EW)
        entry_input.grid(row=0, column=0, padx = 5, pady=5, sticky=tk.EW)

        return entry_input
    
    def make_run_entry(self, parent):
        # Set frames for layout
        frame_paths = ttk.Labelframe(parent, text='Run Folder')
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(index=0, weight=1)

        label = tk.Label(frame_paths, text="Short description:")
        label.grid(row = 0, column=0, padx=5, pady=5, sticky=tk.W)

        entry = tk.Text(frame_paths, height=2, width=10)
        entry.grid(row=1, column=0, padx = 5, sticky=tk.EW)

        entry_input = tk.Entry(frame_paths)
        button_input = tk.Button(frame_paths, text = 'Initialize')
        button_input.configure(command = lambda:self.initialize_run(entry_input, button_input, entry))
        
        entry_input.grid(row=3, column=0, padx = 5, pady=5, sticky=tk.EW)
        button_input.grid(row = 4, column = 0, padx=5, pady=5, sticky=tk.EW)

        return entry_input

    def select_folder(self, entry):
        folder_path = filedialog.askdirectory()
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        self.output_path = folder_path

    def connect_tsi(self, entry, button):
        port = entry.get()
        if button['text'] == "Connect":
            try:
                self.tidal.set_tsi_port(port)
                self.tidal.connect_tsi()
            except:
                print("There was a problem connecting")
            else:
                button['text'] = "Disconnect"
            
        elif button['text'] == "Disconnect":
            try:
                self.tidal.disconnect_tsi()
            except:
                print("There was a problem disconnecting")
            else:
                button['text'] = "Connect"

    def connect_arduino(self, entry, button):
        port = entry.get()
        if button['text'] == "Connect":
            try:
                self.tidal.set_motor_port(port)
                self.tidal.connect_motors()
            except:
                print("There was a problem connecting")
            else:
                button['text'] = "Disconnect"
            
        elif button['text'] == "Disconnect":
            try:
                self.tidal.disconnect_motors()
            except:
                print("There was a problem disconnecting")
            else:
                button['text'] = "Connect"

    def initialize_run(self, path_entry, button, description_entry):
        if button['text'] == "Initialize":
            try:
                # Make a unique ID from the description
                notes = description_entry.get('1.0', tk.END)
                id, date = utils.make_id(notes)
                run_folder, data_folder = utils.make_run_folder(output_dir=self.tidal.get_log_dir(), id = id)
                path_entry.delete(0, tk.END)
                path_entry.insert(0, id)

                # Update values in TIDAL instance
                self.tidal.set_run_id(id)
                self.tidal.set_run_dir(run_folder)
                self.tidal.set_data_dir(data_folder)
                
                # Create the log files
                write_log(dir=run_folder, lines = get_software_version())
                write_log(dir=run_folder, lines=[f"Log created (UTC): {date}", notes])
            except:
                print("There was a problem creating the structure")
            else:
                button['text'] = "Clear"
                print("Run initialized")
            
        elif button['text'] == "Clear":
            # Original intent was to make this a 'conclude' functionality -- future feature
            try:
                # TODO: Stop reading and close flow meter connection
                pass                
            except:
                print("There was a problem clearing the run")
            else:
                print("Run cleared")
                path_entry.delete(0, tk.END)
                description_entry.delete('1.0', tk.END)
                button['text'] = "Initialize"
                



if __name__ == "__main__":
    tidal = TIDAL()
    tidal.set_motor_port('COM8')

    root = tk.Tk()
    root.columnconfigure(0,weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0,weight=1)
    SetupPanel(frame, tidal_instance=tidal)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()