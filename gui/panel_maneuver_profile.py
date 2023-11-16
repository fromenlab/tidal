import tkinter as tk
from tkinter import ttk
from api.arduino_motor import Arduino
from api.TIDAL import TIDAL
from api.lobe import Lobe

class ProfileManeuverPanel:
    def __init__(self, parent, tidal_instance: TIDAL = None):
        self.parent = parent
        self.tidal_instance = tidal_instance
        # Reference to tidal instance. Tidal values will be 
        # updated when these values are changed
        self.ard = tidal_instance.get_motors()
        self.lobes = tidal_instance.lobes
        # self.lobe_entries = tidal_instance.lobe_entries
        self.global_entries = tidal_instance.global_entries
        self.order = tidal_instance.order

        fr_pad = tk.Frame(self.parent)
        fr_pad.grid(padx=10, pady=10, sticky=tk.NSEW)
        fr_pad.columnconfigure(0, weight=1)

        self.make_maneuver_input(parent = fr_pad)

        self.frame = fr_pad

    ###################
    # Utility functions
    ###################

    def get_lobes(self):
        return ''.join([str(lobe.gui_checkbox.get()) for lobe in self.lobes])
    
    def make_lobe_boxes(self, parent, lobes: Lobe):
        fr_checks = tk.Frame(parent)
        fr_checks.grid()

        for index, lobe in enumerate(lobes):
            # fr_checks.columnconfigure(index, weight=1)
            lobe.gui_checkbox = tk.IntVar()
            check = tk.Checkbutton(fr_checks, text = lobe.name, variable=lobe.gui_checkbox)
            check.grid(column=index, row = 0)
    
    def make_maneuver_input(self, parent):
        # maneuvers = ['Inhale', 'Exhale']

        fr = ttk.LabelFrame(parent, text="Position tuning")
        fr.grid(sticky=tk.EW, pady=10)
        fr.columnconfigure(0,weight=1)

        self.make_lobe_boxes(fr, self.lobes)

        fr_maneuver = tk.Frame(fr)
        fr_maneuver.grid()
        fr_maneuver.columnconfigure(0, weight=1)
        fr_maneuver.columnconfigure(1, weight=1)
        fr_maneuver.columnconfigure(2, weight=1)

        inhale_button = tk.Button(fr_maneuver, text = 'Inhale', command=lambda:self.get_lobes())
        exhale_button = tk.Button(fr_maneuver, text = 'Exhale', command=lambda:self.get_lobes())
        entry_steps = tk.Entry(fr_maneuver)
        self.entry_steps = entry_steps

        inhale_button.grid(row = 0, column=0)
        entry_steps.grid(row = 0, column=1, padx=10, pady=10)
        exhale_button.grid(row = 0, column=2)

if __name__ == "__main__":
    # arduino = Arduino('/dev/ttyACM0')

    tidal = TIDAL()
    # tidal.set_motor_port('COM8')
    # tidal.connect_motors()

    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    ProfileManeuverPanel(frame, tidal)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()