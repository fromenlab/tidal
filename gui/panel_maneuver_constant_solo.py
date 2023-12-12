import tkinter as tk
from tkinter import ttk
from api.arduino_motor import Arduino
from api.TIDAL import TIDAL
from api.lobe import Lobe
from gui.VerticalScrolledFrame import VerticalScrolledFrame

class ManeuverPanel:
    def __init__(self, parent, tidal_instance: TIDAL = None):
        self.parent = parent
        self.tidal_instance = tidal_instance
        # Reference to tidal instance. Tidal values will be 
        # updated when these values are changed
        self.ard = tidal_instance.get_motors()
        self.lobes = tidal_instance.lobes

        fr_pad = VerticalScrolledFrame(self.parent, padx=5, pady=5)
        fr_pad.columnconfigure(0, weight=1)

        tk.Label(fr_pad.interior, text="Constant-delay Settings", font=("SansSerif", 18, "bold")).pack()
        self.make_lobe_entries(parent = fr_pad.interior)
        self.hr(fr_pad.interior)
        self.make_profile_buttons(parent = fr_pad.interior)

        self.frame=fr_pad



    ###################
    # Utility functions
    ###################

    def get_lobes(self):
        return ''.join([str(lobe.gui_checkbox.get()) for lobe in self.lobes])

    ##################
    # Layout functions
    ##################

    def hr(self, parent):
        ttk.Separator(parent, orient='horizontal').pack()

    def make_lobe_entries(self, parent):
        lobes_frame = tk.Frame(parent)
        lobes_frame.pack(side = tk.TOP, expand=True, fill=tk.X)
        lobes_frame.columnconfigure(0, weight=1)        

        for lobe in self.lobes:
            lobe_frame = ttk.LabelFrame(lobes_frame, text = lobe.name, padding=(5, 0, 5, 5))
            lobe_frame.grid(sticky=tk.EW, pady=10)
            # lobe_frame.columnconfigure(0, weight=1)
            lobe_frame.columnconfigure(1, weight=1)

            tk.Label(lobe_frame, text="Steps").grid(sticky=tk.EW, column=0, row=0)
            tk.Label(lobe_frame, text="Delay").grid(sticky=tk.EW, column=0, row=1)

            entry_steps = tk.Entry(lobe_frame)
            lobe.gui_constant_step_entry = entry_steps
            entry_delay = tk.Entry(lobe_frame)
            lobe.gui_constant_delay_entry = entry_delay

            entry_steps.grid(row=0, column=1, padx=5, sticky=tk.EW)
            entry_delay.grid(row=1, column=1, padx=5, sticky=tk.EW)


    def make_profile_buttons(self, parent):
        profile_frame = tk.Frame(parent)
        profile_frame.pack(side = tk.TOP, expand=True, fill=tk.X)
        profile_frame.columnconfigure(0, weight=1)

        button_update = tk.Button(profile_frame, text = 'Push to Controller', command = self.update_lobe_settings)
        button_run = tk.Button(profile_frame, text = 'Run Constant Profile', command = self.run, height = 3)

        button_update.grid(padx=5, pady=5, sticky=tk.EW)
        button_run.grid(padx=5, pady=5, sticky=tk.EW)

    #########################
    # Action/Output functions
    #########################

    def update_lobe_settings(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return

        for index, lobe in enumerate(self.lobes):
            selected_lobe = [0,0,0,0,0]
            selected_lobe[index] = 1
            selected_lobe = ''.join([str(_) for _ in selected_lobe])

            if lobe.gui_constant_step_entry.get():
                Arduino.set_lobe_default(self.ard, 'steps', lobe.gui_constant_step_entry.get(), selected_lobe)

            if lobe.gui_constant_delay_entry.get():
                Arduino.set_lobe_default(self.ard, 'delay', lobe.gui_constant_delay_entry.get(), selected_lobe)
        
        Arduino.update_lobe_delays(self.ard)

    def check_settings(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return

        self.ard.print_parameters()
        self.ard.print_lobe_delays()

    def run(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return

        print("Running constant profile...")
        self.ard.print_parameters()
        self.ard.run_profile_constant()

if __name__ == "__main__":
    # arduino = Arduino('/dev/ttyACM0')

    tidal = TIDAL()
    # tidal.set_motor_port('COM8')
    # tidal.connect_motors()

    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    panel = ManeuverPanel(frame, tidal)
    panel.frame.pack(expand=True, fill = tk.BOTH)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()