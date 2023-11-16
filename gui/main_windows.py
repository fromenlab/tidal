import tkinter as tk
from tkinter import ttk

from gui.panel_maneuver import ManeuverPanel
import gui.panel_flow_recorder_windows as recorder
from gui.panel_plot import PlotPanel
from api.arduino_motor import Arduino
from api.tsi import TSI
import gui.panel_interactive as interactive
from gui.panel_bezier import BezierPanel
from gui.panel_console import LogPanel


if __name__ == "__main__":

    from api.TIDAL import TIDAL
    # TIDAL setup

    tidal = TIDAL()
    # tidal.set_motor_port('COM3')
    # tidal.connect_motors()
    # tidal.set_tsi_port('COM7')

    ###
    # Communications setup
    ###

    # arduino_instance = Arduino('COM8')
    # tsi_instance = TSI('COM7')

    

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

    fr_left = tk.Frame(root, width=root.winfo_width()/2, highlightbackground="blue", highlightthickness=2)
    fr_right = tk.Frame(root, width=root.winfo_width()/2, highlightbackground="blue", highlightthickness=2)

    fr_left.columnconfigure(0, weight=1)
    fr_right.columnconfigure(0, weight=1)

    fr_left.grid(column=0, row = 0, sticky=tk.NSEW)
    fr_right.grid(column=1, row = 0, sticky=tk.NSEW)

    fr_flow = tk.Frame(fr_left, width=100)#, highlightbackground="blue", highlightthickness=2)
    fr_flow.columnconfigure(0, weight=1)
    fr_maneuver = tk.Frame(fr_right, width=100, height=100)
    fr_maneuver.columnconfigure(0, weight=1)
    fr_plot = tk.Frame(fr_left, width=100)
    fr_plot.columnconfigure(0, weight=1)
    fr_curve = tk.Frame(fr_left, width=100, height=100)
    fr_log = tk.Frame(fr_right)
    fr_log.columnconfigure(0, weight=1)

    recorder_panel = recorder.RecorderPanel(fr_flow, tidal)
    maneuver_panel = ManeuverPanel(fr_maneuver, tidal)
    plot_panel = PlotPanel(fr_plot)
    log_panel = LogPanel(fr_log)
    # interactive_panel = interactive.InteractivePolygonPanel(fr_curve)
    # bezier_panel = BezierPanel(fr_curve)

    n = ttk.Notebook(fr_curve)
    n.pack(fill='both', expand=True)
    lobes = {
            'RU': 0,
            'RM': 0,
            'RL': 0,
            'LU': 0,
            'LL': 0
        }
    for lobe in lobes:
        fr = ttk.Frame(n)
        n.add(fr, text=lobe)
        BezierPanel(fr)

    ###
    # Layout setup
    ###

    fr_flow.grid(padx=10, pady=10, sticky=(tk.N, tk.EW), column=0, row=0)
    fr_maneuver.pack(fill='x')
    fr_plot.grid(padx=10, sticky=(tk.EW, tk.N), column=0, row=1)
    fr_curve.grid(padx=10, sticky=tk.EW, column=0, row=2)
    fr_log.pack(expand=True, fill='both', padx=10, pady=10)
    root.rowconfigure(2,weight=1)

    root.mainloop()