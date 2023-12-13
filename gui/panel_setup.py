import os
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
        fr.pack(expand=True,fill=tk.BOTH)
        fr.columnconfigure(0,weight=1)

        self.make_log_entry(fr)
        self.make_run_entry(fr)
        self.make_config_entry(fr)
        self.make_tsi_entry(fr)
        self.make_arduino_entry(fr)
        self.make_instructions_entry(fr)

    def make_config_entry(self, parent):
        frame_config = ttk.Labelframe(parent, text = 'Configuration')
        button_load = tk.Button(frame_config, text = 'Load', command = lambda:self.tidal.load())
        button_save = tk.Button(frame_config, text = 'Save', command = lambda:self.tidal.save())

        button_load.pack(side = tk.LEFT, padx=5, expand = True, fill = tk.X, pady=5)
        button_save.pack(side = tk.LEFT, padx=5, expand = True, fill = tk.X, pady=5)
        frame_config.pack(fill=tk.X)

    def make_log_entry(self, parent):
        # Set frames for layout
        frame_paths = ttk.Labelframe(parent, text='Log Folder')
        frame_paths.pack(fill=tk.X)
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
        frame_paths.pack(fill=tk.X)
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
        frame_paths.pack(fill=tk.X)
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
        frame_paths = ttk.Labelframe(parent, text='Run Info')
        frame_paths.pack(fill=tk.X)
        frame_paths.columnconfigure(index=0, weight=1)

        label = tk.Label(frame_paths, text="Short description:")
        label.pack(padx=5, pady=5, anchor=tk.W)

        entry = tk.Text(frame_paths, height=1, width=10)
        entry.pack(padx = 5, fill=tk.X)

        id_input = tk.Entry(frame_paths, state='readonly', justify=tk.CENTER)
        button_input = tk.Button(frame_paths, text = 'Initialize')
        button_input.configure(command = lambda:self.initialize_run(id_input, button_input, entry))
        
        button_input.pack(padx=5, pady=5, fill=tk.X)
        id_input.pack(padx = 5, pady=5, fill=tk.X)

        # Notes
        label_notes = tk.Label(frame_paths, text="Notes:")
        label_notes.pack(padx=5, anchor=tk.W)
        notes = tk.Text(frame_paths, height=3, width=10)
        notes.pack(padx=5, pady=5, fill=tk.BOTH)

        self.run_notes = notes

        return id_input
    
    def make_instructions_entry(self, parent):
        instructions = tk.Label(parent, justify = tk.LEFT)
        contents = tk.StringVar()
        instructions['textvariable'] = contents
        
        lines = [
            'Basic run protocol:',
            '- Set a log folder',
            '- Initialize a new run',
            '- Load a configuration',
            '- Push to controller',
            '- Check parameters',
            '- Run profile'
        ]

        contents.set('\n'.join(lines))

        instructions.pack(side=tk.BOTTOM, anchor=tk.W, padx=5, pady=5)
        # instructions.grid(sticky=tk.S)

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
                path_entry.configure(state='normal')
                path_entry.delete(0, tk.END)
                path_entry.insert(0, id)
                path_entry.configure(state='readonly')

                # Update values in TIDAL instance
                self.tidal.set_run_id(id)
                self.tidal.set_run_dir(run_folder)
                self.tidal.set_data_dir(data_folder)
                
                # Create the log files
                write_log(dir=run_folder, lines = get_software_version())
                write_log(dir=run_folder, lines=[f"\nLog created (UTC): {date}", notes])
            except Exception as e:
                print("There was a problem creating the structure")
                print(e)
            else:
                button['text'] = "Clear"
                print(f"Run initialized: {id}")
            
        elif button['text'] == "Clear":
            # Original intent was to make this a 'conclude' functionality -- future feature
            # TODO: Stop reading and close flow meter connection
            try:
                # Save configuration in run folder
                self.tidal.save(filename = f"config-{self.tidal.get_run_id()}.tidal")
                print("Run notes:")
                print(self.run_notes.get('1.0', tk.END))

                # Reset log settings
                self.tidal.set_run_dir(os.path.join(self.tidal.log_dir, "runs"))
            except Exception as e:
                print("There was a problem clearing the run")
                print(e)
            else:
                print("Run cleared")
                path_entry.configure(state='normal')
                path_entry.delete(0, tk.END)
                path_entry.configure(state='readonly')
                description_entry.delete('1.0', tk.END)
                self.run_notes.delete('1.0', tk.END)
                button['text'] = "Initialize"
                



if __name__ == "__main__":
    tidal = TIDAL()
    # tidal.set_motor_port('COM8')

    root = tk.Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0, weight=1)
    SetupPanel(frame, tidal_instance=tidal)
    # frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)
    frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    root.mainloop()