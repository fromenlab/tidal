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

        log_event = Event()
        live_event = Event()

        # Run options
        button_live = tk.Button(frame_run, text = 'Plot Live', command = lambda:run_plot_live(self.tidal, self, live_event), padx=10, pady=10)
        button_live.pack(padx=10, pady=10, fill=tk.X)

        button_run = tk.Button(frame_run, text = 'Start Recording', command = lambda:run(self.tidal, self, log_event, live_event), padx=10, pady=10)
        button_run.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

        # Stop options
        button_terminate = tk.Button(frame_run, text = 'Terminate', command = lambda:stop(log_event, live_event), padx=10, pady=10)
        button_terminate.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X)

        # Update
        button_log = tk.Button(frame_run, text = 'Update Flow Log', command = self.update_log, padx=10, pady=10)
        button_log.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X)

    def update_log(self):
        utils.logger.write_log(dir=self.tidal.get_run_dir(), name = "flow-log.txt", lines = self.get_log_lines(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")))

log_process = None

def run(tidal: TIDAL, panel, log_event, live_event):
    global log_process
    utils.logger.write_log(dir=tidal.get_run_dir(), name="flow-log.txt", lines=panel.get_log_lines(date=''))

    if log_process is not None and log_process.is_alive():
        print("Stopping existing log process. Any data in current queue will be lost.")
        if live_event.is_set():
            live_event.clear()
        log_process.terminate()

    if tidal.tsi_connected:
        print("Disconnecting flow meter for transfer to a new process.")
        tidal.disconnect_tsi() # Disconnect for multiprocessing to pickle (if sending tidal)
    
    tidal.get_tsi().set_output_dir(tidal.get_data_dir()) # breaks standalone behavior
    log_process = Process(target=log_data, args=(tidal.get_tsi(), tidal.log_file, log_event,))
    print("Starting data collection process.")
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

    tsi_instance.close()
    event.clear()

def run_plot_live(tidal: TIDAL, panel, live_event):
    global log_process
    if log_process is not None and log_process.is_alive():
        print("There is currently a log process running. A new live plot will not be generated.")
        return
    if tidal.tsi_connected:
        tidal.disconnect_tsi() # Disconnect for multiprocessing to pickle (if sending tidal)

    print("Preparing live plot... (Data not recorded.)")
    log_process = Process(target=plot_live, args=(tidal.get_tsi(), live_event))
    log_process.start()
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
    

def plot_live(tsi_instance: TSI, live_event):
    # References
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
    # https://matplotlib.org/stable/api/animation_api.html
    # https://matplotlib.org/stable/gallery/animation/simple_anim.html

    live_event.set()

    # Set up plot
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(xlim=(0,100), ylim=(0,60))
    ax.xaxis.set_ticks([])
    ax.set_ylabel("Flow rate (SLPM)")
    lines = ax.plot([], [])[0]

    tsi_instance.connect()
    tsi_instance.live = True
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
    # _not_ not show accurate time
    plt.show()

    # After closing the plot window
    tsi_instance.live = False
    live_event.clear()
    tsi_instance.close()
    
def stop(log_event, live_event):
    # Stop logging
    global log_process

    if live_event.is_set() and log_process is not None and log_process.is_alive():
        print("Terminating live plot.")
        live_event.clear()
        log_process.terminate()
    elif log_process is not None and log_process.is_alive():
        print("Stopping data collection. Please wait for the current data series to complete...")
        log_event.set()
        while log_event.is_set():
            log_event.wait(0.5)
        print("Data collection complete.")
    else:
        print("There was nothing to terminate.")

    return