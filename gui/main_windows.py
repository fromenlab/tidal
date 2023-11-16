import tkinter as tk

from gui.panel_maneuver import ManeuverPanel
import gui.panel_flow_recorder_windows as recorder
from gui.panel_plot import PlotPanel
from api.arduino_motor import Arduino
from api.tsi import TSI_Win as TSI
import gui.panel_interactive as interactive
from gui.panel_bezier import BezierPanel


if __name__ == "__main__":

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

    fr_1 = tk.Frame(root, width=100)#, highlightbackground="blue", highlightthickness=2)
    fr_1.columnconfigure(0, weight=1)
    fr_2 = tk.Frame(root, width=100, height=100)
    fr_2.columnconfigure(0, weight=1)
    fr_plot = tk.Frame(root, width=100)
    fr_plot.columnconfigure(0, weight=1)
    fr_curve = tk.Frame(root, width=100, height=100)

    recorder_panel = recorder.RecorderPanel(fr_1)#, tsi_instance=tsi_instance)
    maneuver_panel = ManeuverPanel(fr_2)#, arduino_instance=arduino_instance)
    plot_panel = PlotPanel(fr_plot)
    # interactive_panel = interactive.InteractivePolygonPanel(fr_curve)
    bezier_panel = BezierPanel(fr_curve)


    ###
    # Layout setup
    ###

    fr_1.grid(padx=10, pady=10, sticky=(tk.N, tk.EW), column=0, row=0)
    fr_2.grid(padx=10, pady=10, sticky=tk.NSEW, column=1, row=0, rowspan=3)
    fr_plot.grid(padx=10, sticky=(tk.EW, tk.N), column=0, row=1)
    fr_curve.grid(padx=10, sticky=tk.EW, column=0, row=2)
    root.rowconfigure(2,weight=1)

    root.mainloop()