import tkinter as tk
from tkinter import ttk
from api.arduino_motor import Arduino
from api.TIDAL import TIDAL
from api.lobe import Lobe
from gui.VerticalScrolledFrame import VerticalScrolledFrame

class ProfileManeuverPanel:
    def __init__(self, parent, tidal_instance: TIDAL = None):
        self.parent = parent
        self.tidal_instance = tidal_instance
        self.ard = tidal_instance.get_motors()
        self.lobes = tidal_instance.lobes
        self.global_entries = tidal_instance.global_entries
        self.order = tidal_instance.order_entry

        fr_pad = VerticalScrolledFrame(self.parent,
                                       padx = 5, pady = 5)#,
                        #   highlightbackground="blue", highlightthickness=2)
        fr_pad.columnconfigure(0, weight=1)

        tk.Label(fr_pad.interior, text="Variable-delay Settings", font=("SansSerif", 18, "bold")).pack()
        self.make_lobe_param_views(fr_pad.interior)
        self.make_profile_buttons(fr_pad.interior)

        self.frame = fr_pad

    def make_lobe_param_views(self, parent):
        lobes_frame = tk.Frame(parent)
        lobes_frame.pack(side = tk.TOP, expand=True, fill=tk.X)
        lobes_frame.columnconfigure(0, weight=1)
        rows = 0

        for lobe in self.lobes:
            # print(lobe.name)
            # Bounding frame
            lobe_frame = ttk.LabelFrame(lobes_frame, text = lobe.name)
            lobe_frame.grid(row = rows, sticky=tk.EW, pady=10)
            # lobe_frame.columnconfigure(0, weight=1)
            lobe_frame.columnconfigure(1, weight=1)
            rows += 1
            
            # Step entry
            tk.Label(lobe_frame, text = "Steps").grid(sticky=tk.W, column=0, row=0, padx=5)
            entry_steps = tk.Entry(lobe_frame)
            lobe.gui_variable_step_entry = entry_steps
            entry_steps.grid(row = 0, column = 1, sticky=tk.EW, padx=5)

            # Delay labels - hard-coded
            delay_frame = tk.Frame(lobe_frame, pady=5)
            delay_frame.grid(row = 1, column = 0, columnspan=2, sticky=tk.EW)
            delay_frame.columnconfigure(1, weight=1)
            delay_frame.columnconfigure(2, weight=1)
            
            tk.Label(delay_frame, text = "Delays").grid(sticky=tk.NW, column=0, row=0, padx=5, pady=5)
            tk.Label(delay_frame, text = "Inhale").grid(sticky=tk.W, column=0, row=1, padx=10)
            tk.Label(delay_frame, text = "Exhale").grid(sticky=tk.W, column=0, row=2, padx=10)
            tk.Label(delay_frame, text = "Min", anchor = "center").grid(sticky=tk.EW, column=1, row=0, padx=10)
            tk.Label(delay_frame, text = "Max", anchor = "center").grid(sticky=tk.EW, column=2, row=0, padx=10)

            # Delay entries
            entry_imin = tk.Entry(delay_frame)
            entry_imax = tk.Entry(delay_frame)

            entry_emin = tk.Entry(delay_frame)
            entry_emax = tk.Entry(delay_frame)

            entry_imin.grid(row = 1, column = 1, sticky=tk.EW)
            entry_imax.grid(row = 1, column=2, sticky=tk.EW)
            entry_emin.grid(row=2,column=1,sticky=tk.EW)
            entry_emax.grid(row=2, column=2, sticky=tk.EW)

            # Connect to lobe
            lobe.gui_variable_inhale_min_delay_entry = entry_imin
            lobe.gui_variable_inhale_max_delay_entry = entry_imax
            lobe.gui_variable_exhale_min_delay_entry = entry_emin
            lobe.gui_variable_exhale_max_delay_entry = entry_emax
            
    def make_profile_buttons(self, parent):
        profile_frame = tk.Frame(parent)
        profile_frame.pack(side = tk.TOP, expand=True, fill=tk.X)
        profile_frame.columnconfigure(0, weight=1)

        button_update = tk.Button(profile_frame, text = 'Push to Controller', command = self.update_profile)
        button_run = tk.Button(profile_frame, text = 'Run Variable Profile', command = self.run, height = 3)

        button_update.grid(row = 0, padx=5, pady=5, sticky=tk.EW)
        button_run.grid(row = 1, padx=5, pady=5, sticky=tk.EW)

    def update_profile(self):
        print("Updating profiles...")
        for lobe in self.lobes:
            print(f"Updating {lobe.name}...")
            lobe.update_variable_profile_params()
        
        print("Writing file...")
        self.tidal_instance.update_variable_profile()

        # Send sequences to update global settings and step count
        self.update_global_settings()
        self.update_lobe_settings()

        print("Done")

    def update_global_settings(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return
        
        if self.global_entries['Breath count'].get():
            Arduino.set_breath_count(self.ard, self.global_entries['Breath count'].get())
        if self.global_entries['Profile delay (s)'].get():
            Arduino.set_delay(self.ard, maneuver='profile', delay=self.global_entries['Profile delay (s)'].get())
        if self.global_entries['Delay inhale (s)'].get():
            Arduino.set_delay(self.ard, maneuver='inhale', delay=self.global_entries['Delay inhale (s)'].get())
        if self.global_entries['Delay exhale (s)'].get():
            Arduino.set_delay(self.ard, maneuver='exhale', delay=self.global_entries['Delay exhale (s)'].get())
        
        Arduino.set_maneuver_order(self.ard, maneuver= 'exhale' if self.order.current() == 0 else 'inhale')
        
    def update_lobe_settings(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return

        for index, lobe in enumerate(self.lobes):
            selected_lobe = [0,0,0,0,0]
            selected_lobe[index] = 1
            selected_lobe = ''.join([str(_) for _ in selected_lobe])

            if lobe.gui_variable_step_entry.get():
                self.ard.set_lobe_default('steps', lobe.step_count_variable, selected_lobe)

    def run(self):
        if not self.tidal_instance.motors_connected:
            print("Please connect the motor controller. Cancelling command.")
            return

        print("Running variable profile...")
        self.ard.print_parameters()
        self.ard.run_profile_variable()


if __name__ == "__main__":
    # arduino = Arduino('/dev/ttyACM0')

    tidal = TIDAL()
    # tidal.set_motor_port('COM8')
    # tidal.connect_motors()

    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    panel = ProfileManeuverPanel(frame, tidal)
    panel.frame.pack(expand=True, fill = tk.X, anchor = tk.NW)
    frame.grid()

    root.mainloop()