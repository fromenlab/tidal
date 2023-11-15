import tkinter as tk
from tkinter import filedialog
from multiprocessing import Process
from datetime import datetime

from api.tsi import TSI_Win as TSI
import utils.unique_id as utils

class RecorderPanel:
    def __init__(self, parent, tsi_instance = None):
        self.parent = parent
        self.tsi = tsi_instance
        self.log_process = None
        self.output_path = None     # Folder for all logs
        self.run_folder = None      # Folder for given log
        self.conditions = {
            "Device ID": None, 
            "Alignment": None, 
            "Temperature (C)": None, 
            "Relative Humidity (%)": None
            }

        fr_pad = tk.Frame(self.parent)
        fr_pad.grid(padx=10, pady=10, sticky=tk.NSEW)
        fr_pad.columnconfigure(0,weight=1)

        self.entry_input = self.make_path_entry(fr_pad)
        self.make_conditions_entry(fr_pad)
        self.notes = self.make_text_entry(fr_pad)
        self.make_run_frame(fr_pad)

    def make_text_entry(self, parent):
            # Set frames for layout
        frame_text = tk.Frame(parent)
        frame_text.grid(sticky = tk.EW)
        frame_text.columnconfigure(0,weight=1)
        
        label = tk.Label(frame_text, text="Notes:")
        label.grid(row = 0, column=0, padx=5, pady=5, sticky=tk.W)

        entry = tk.Text(frame_text, height=5)
        entry.grid(row=1, column=0, padx = 5, sticky=tk.EW)

        return entry
    
    def get_notes(self):
        return self.notes.get('1.0', 'end')
    
    def get_conditions(self):
        conditions = [f"{condition}: {str(self.conditions[condition].get())}" for condition in self.conditions]

        return conditions
    
    def get_log_lines(self, date = None):
        lines = []
        lines.append(date)
        for _ in self.get_conditions():
            lines.append(_)
        lines.append("Notes: ")
        lines.append(self.get_notes())
        print(lines)

        return lines
    
    def make_conditions_entry(self, parent):
        frame = tk.Frame(parent)
        frame.grid(sticky=tk.EW)
        frame.columnconfigure(1, weight=1)

        for index, condition in enumerate(self.conditions):
            label = tk.Label(frame, text=condition)
            label.grid(row = index, column=0, padx=5, pady=5, sticky=tk.W)

            entry = tk.Entry(frame)
            entry.grid(row=index, column=1, padx = 5, sticky=tk.EW)

            self.conditions[condition] = entry


    def make_path_entry(self, parent):
            # Set frames for layout
        frame_paths = tk.Frame(parent)
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(index=1, weight=1)

        button_input = tk.Button(frame_paths, text = 'Log Folder', command = lambda:self.select_folder(entry_input))
        button_input.grid(row = 0, column = 0, padx=5, sticky=tk.EW)
        entry_input = tk.Entry(frame_paths)
        entry_input.grid(row=0, column=1, padx = 5, sticky=tk.EW)

        return entry_input

    def select_folder(self, entry):
        folder_path = filedialog.askdirectory()
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        self.output_path = folder_path

    def make_run_frame(self, parent):

        frame_run = tk.Frame(parent)
        frame_run.grid(sticky=tk.EW)
        frame_run.columnconfigure(0, weight=1)

        # Run options
        button_run = tk.Button(frame_run, text = 'Start Logging', command = lambda:run(self.tsi, self), padx=10, pady=10)
        button_run.grid(column=0, row = 0, padx=10, pady=10, sticky=tk.EW)

        # Stop options
        button_terminate = tk.Button(frame_run, text = 'Terminate', command = stop, padx=10, pady=10)
        button_terminate.grid(column=1, row = 0, padx=10, pady=5, sticky=tk.EW)

        button_log = tk.Button(frame_run, text = 'Update Log', command = self.update_log, padx=10, pady=10)
        button_log.grid(column=2, row = 0, padx=10, pady=10, sticky=tk.EW)

    def update_log(self):
        utils.write_log(dir=self.run_folder, name = "flow-log.txt", lines = self.get_log_lines(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")), mode='a')

log_process = None

def run(tsi, panel):
    print("Run clicked")
    global log_process
    notes = panel.get_notes()
    id, date = utils.make_id(notes)
    output_dir = panel.entry_input.get()
    panel.run_folder, panel.data_folder = utils.make_run_folder(output_dir=output_dir, id = id)
    utils.write_log(dir=panel.run_folder, name="flow-log.txt", lines=panel.get_log_lines(date=date))
    panel.tsi.set_output_dir(panel.data_folder)
    log_process = Process(target=log_data, args=(tsi,))
    log_process.start()
    return

def log_data(tsi_instance):
    # Read and save set of 1000 flow measurements until terminated

    tsi_instance.establish_connection()
    response = tsi_instance.query_connection(message="SSR0010\r")
    print(f'Set sample rate: {response}')

    # Confirm sample rate
    response = tsi_instance.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    while True:
        tsi_instance.query_flow_set()
    
def stop():
    # Stop logging
    global log_process
    # TODO: Clean handling of log termination. Should finish recording all remaining data before terminating process.
    log_process.terminate()
    return

if __name__ == "__main__":
    tsi = TSI('COM7')

    root = tk.Tk()
    root.columnconfigure(0,weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0,weight=1)
    RecorderPanel(frame, tsi_instance=tsi)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()