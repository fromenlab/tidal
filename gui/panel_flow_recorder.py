import tkinter as tk
from tkinter import filedialog
from multiprocessing import Process, Event
from datetime import datetime

from api.tsi import TSI
import utils.logger
from api.TIDAL import TIDAL

class RecorderPanel:
    def __init__(self, parent, tidal_instance: TIDAL = None):
        self.parent = parent
        self.tidal = tidal_instance
        self.tsi = tidal_instance.get_tsi()
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

    def make_run_frame(self, parent):

        frame_run = tk.Frame(parent)
        frame_run.grid(sticky=tk.EW)
        frame_run.columnconfigure(0, weight=1)

        event = Event()

        # Run options
        button_run = tk.Button(frame_run, text = 'Start Recording', command = lambda:run(self.tidal, self, event), padx=10, pady=10)
        button_run.grid(column=0, row = 0, padx=10, pady=10, sticky=tk.EW)

        button_live = tk.Button(frame_run, text = 'Plot Live', command = lambda:run_plot_live(self.tidal, self, event), padx=10, pady=10)
        button_live.grid(column=0, row=1, padx=10, pady=5, sticky=tk.EW)

        # Stop options
        button_terminate = tk.Button(frame_run, text = 'Terminate', command = lambda:stop(event), padx=10, pady=10)
        button_terminate.grid(column=1, row = 0, padx=10, pady=5, sticky=tk.EW)

        button_log = tk.Button(frame_run, text = 'Update Log', command = self.update_log, padx=10, pady=10)
        button_log.grid(column=2, row = 0, padx=10, pady=10, sticky=tk.EW)

    def update_log(self):
        utils.logger.write_log(dir=self.run_folder, name = "flow-log.txt", lines = self.get_log_lines(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")), mode='a')

log_process = None

def run(tidal: TIDAL, panel, event):
    print("Run clicked")
    global log_process
    utils.logger.write_log(dir=tidal.get_run_dir(), name="flow-log.txt", lines=panel.get_log_lines(date=''))

    if tidal.tsi_connected:
        tidal.disconnect_tsi() # Disconnect for multiprocessing to pickle (if sending tidal)
    if log_process is not None:
        log_process.terminate()

    tidal.get_tsi().set_output_dir(tidal.get_data_dir()) # breaks standalone behavior
    log_process = Process(target=log_data, args=(tidal.get_tsi(), tidal.log_file, event,))
    log_process.start()
    # log_data(tidal.get_tsi(), event)
    return

def log_data(tsi_instance: TSI, log_file, event):
    if log_file is not None:
        import sys
        from utils.logger import Logger
        sys.stdout = Logger(file_output=log_file)

    # Read and save set of 1000 flow measurements until terminated
    tsi_instance.connect()

    response = tsi_instance.query_connection(message="SSR0010\r")
    print(f'Set sample rate: {response}')

    # Confirm sample rate
    response = tsi_instance.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    while not event.is_set():
        tsi_instance.query_flow_set()

    print("Logging complete")
    tsi_instance.close()
    event.clear()

def run_plot_live(tidal: TIDAL, panel, event):
    global log_process
    if tidal.tsi_connected:
        tidal.disconnect_tsi() # Disconnect for multiprocessing to pickle (if sending tidal)
    if log_process is not None:
        log_process.terminate()
    # log_process = Process(target=plot_live, args=(tidal.get_tsi(), event,))
    # log_process.start()
    plot_live(tidal.get_tsi(), event)
    return

from collections import deque
class TSIPlot:
    def __init__(self) -> None:
        self.plot_length = 100
        self.maxy = 60
        self.x = range(self.plot_length)
        self.y = deque([0]*self.plot_length, maxlen=self.plot_length)
        self.line = None
        self.currentTimer = 0
        self.previousTimer = 0

def update_plot(frame, tsi_instance: TSI, plot_instance: TSIPlot):
    value = tsi_instance.convert_single()
    if value and value < plot_instance.maxy:
        plot_instance.y.append(value)
        plot_instance.line.set_data(plot_instance.x, plot_instance.y)
    

def plot_live(tsi_instance: TSI, event):
    # References
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
    # https://matplotlib.org/stable/api/animation_api.html
    # https://matplotlib.org/stable/gallery/animation/simple_anim.html

    print("Displaying live plot. Data not recorded.")

    # Set up plot
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(xlim=(0,100), ylim=(0,60))
    ax.xaxis.set_ticks([])
    ax.set_ylabel("Flow rate (SLPM)")
    lines = ax.plot([], [])[0]

    tsi_instance.connect()
    response = tsi_instance.query_connection(message="SSR0010\r")
    print(f'Set sample rate: {response}')

    # Confirm sample rate
    response = tsi_instance.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    tsi_instance.setup_single()

    plot_instance = TSIPlot()
    plot_instance.line = lines

    anim = FuncAnimation(fig, update_plot, fargs=(tsi_instance, plot_instance), interval=50)
    # Note that update interval will not be exactly 50 ms, and plot data will
    # _not_ be temporally accurate
    plt.show()

    # After closing the plot window
    event.clear()
    tsi_instance.close()
    
def stop(event):
    # Stop logging
    print("Stopping data collection...")
    event.set()
    return