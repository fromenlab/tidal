import tkinter as tk
from tkinter import ttk

from gui.panel_maneuver_constant import ManeuverPanel
import gui.panel_flow_recorder as recorder
from gui.panel_plot import PlotPanel
from gui.panel_maneuver_profile import ProfileManeuverPanel
from gui.panel_bezier import BezierPanel
from gui.panel_console import LogPanel
from gui.panel_setup import SetupPanel
from api.TIDAL import TIDAL
import multiprocessing

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    tidal = TIDAL(tsi_port='/dev/ttyACM0', motor_port='/dev/ttyACM1')

    root = tk.Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0, weight=1)

    minh = root.winfo_vrootheight()/10
    minw = root.winfo_vrootwidth()/10

    # ttk.Panedwindow showed limited configuration for sash on Windows, Conda python
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/panedwindow.html

    pane_main = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief='flat', sashwidth = 5, background = "#3845d1", borderwidth = 0)
    f1 = tk.Frame(pane_main)#, highlightbackground="blue", highlightthickness=2)
    f1.columnconfigure(0, weight=1)
    f2 = tk.Frame(pane_main)#, highlightbackground="blue", highlightthickness=2)
    f2.columnconfigure(0,weight=1)
    f2.rowconfigure(0,weight=1)   
    pane_main.add(f1, minsize = minw, stretch='always')
    pane_main.add(f2, minsize = minw, stretch='always')

    pane_main.grid(sticky=tk.NSEW)

    pane_interact = tk.PanedWindow(f2, orient=tk.VERTICAL, sashrelief='flat', sashwidth = 5, background = "#3845d1", borderwidth = 0)
    frame_notebook = tk.Frame(pane_interact, height=minh*9)#, highlightbackground="blue", highlightthickness=2)
    frame_console_out = tk.Frame(pane_interact, pady=2)#, height=100, highlightbackground="blue", highlightthickness=2)
    pane_interact.add(frame_notebook, minsize = minh, stretch = 'always')
    pane_interact.add(frame_console_out, minsize = 10, stretch = 'never')

    pane_interact.grid(sticky=tk.NSEW)
    pane_interact.rowconfigure(0,weight=1)

    panel_notebook = ttk.Notebook(frame_notebook)
    panel_notebook.pack(fill='both', expand=True)

    frm = ttk.Frame(panel_notebook, padding=5)
    panel_notebook.add(frm, text="Maneuver")
    maneuver_panel = ManeuverPanel(frm, tidal)
    profile_maneuver_panel = ProfileManeuverPanel(frm, tidal)
    maneuver_panel.frame.pack(side=tk.LEFT, anchor=tk.NW, expand=True, fill = tk.BOTH)
    profile_maneuver_panel.frame.pack(side=tk.LEFT, anchor=tk.NE, expand=True, fill = tk.BOTH)
    # profile_maneuver_panel.frame.pack(side=tk.LEFT, anchor=tk.NE)
    # profile_maneuver_panel.frame.grid(row=0, column=1, sticky=tk.NSEW)
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)

    frf = ttk.Frame(panel_notebook)
    panel_notebook.add(frf, text="Flow Meter")
    recorder_panel = recorder.RecorderPanel(frf, tidal)
    plot_panel = PlotPanel(frf)

    for lobe in tidal.lobes:
        fr = ttk.Frame(panel_notebook)
        fr.columnconfigure(0, weight=1)
        fr.columnconfigure(1, weight=1)
        panel_notebook.add(fr, text=lobe.name)
        fr_inhale = ttk.Frame(fr)
        fr_inhale.columnconfigure(0, weight=1)
        fr_exhale = ttk.Frame(fr)
        fr_exhale.columnconfigure(0, weight=1)
        lobe.gui_inhale_bezier = BezierPanel(fr_inhale, plot_title="Inhale")
        lobe.gui_exhale_bezier = BezierPanel(fr_exhale, plot_title="Exhale")
        fr_inhale.grid(column=0, sticky=tk.EW, padx=10)
        fr_exhale.grid(column=1, row=0, sticky=tk.EW, padx=10)
        fr.rowconfigure(0, weight=1)

    log_panel = LogPanel(frame_console_out, tidal)
    setup_panel = SetupPanel(f1, tidal)


    root.mainloop()