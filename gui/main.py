import tkinter as tk

from gui.panel_maneuver import ManeuverPanel
from gui.panel_flow_recorder import RecorderPanel
from gui.panel_plot import PlotPanel
from api.arduino_motor import Arduino
from api.tsi import TSI

if __name__ == "__main__":

    ###
    # Communications setup
    ###

    arduino_instance = Arduino('/dev/ttyACM0')
    tsi_instance = TSI('/dev/ttyUSB0')

    response = tsi_instance.query_connection(message="SSR0010\r")
    print(f'Set sample rate: {response}')

    # Confirm sample rate
    response = tsi_instance.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    ###
    # GUI setup
    ###

    root = tk.Tk()
    # root.geometry('250x230+200+200')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    ###
    # Frame setup
    ###

    fr_1 = tk.Frame(root, width=100, height=100)#, highlightbackground="blue", highlightthickness=2)
    fr_1.columnconfigure(0, weight=1)
    fr_2 = tk.Frame(root, width=100, height=100)
    fr_2.columnconfigure(0, weight=1)
    fr_plot = tk.Frame(root, width=100, height=100)
    fr_plot.columnconfigure(0, weight=1)

    recorder_panel = RecorderPanel(fr_1, tsi_instance=tsi_instance)
    maneuver_panel = ManeuverPanel(fr_2, arduino_instance=arduino_instance)
    plot_panel = PlotPanel(fr_plot)

    ###
    # Layout setup
    ###

    fr_1.grid(padx=10, pady=10, sticky=(tk.N, tk.EW), column=0, row=0)
    fr_2.grid(padx=10, pady=10, sticky=tk.NSEW, column=1, row=0, rowspan=2)
    fr_plot.grid(padx=10, sticky=(tk.EW, tk.N), column=0, row=1)
    root.rowconfigure(1,weight=1)

    root.mainloop()