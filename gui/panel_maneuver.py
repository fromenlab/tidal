import tkinter as tk
from tkinter import ttk
from api.arduino_motor import Arduino

class ManeuverPanel:
    def __init__(self, parent, arduino_instance = None):
        self.parent = parent
        self.ard = arduino_instance
        self.lobes = {
            'RU': 0,
            'RM': 0,
            'RL': 0,
            'LU': 0,
            'LL': 0
        }

        self.lobe_entries = {
            'RU': {
                'steps': None,
                'delay': None
            },
            'RM': {
                'steps': None,
                'delay': None
            },
            'RL': {
                'steps': None,
                'delay': None
            },
            'LU': {
                'steps': None,
                'delay': None
            },
            'LL': {
                'steps': None,
                'delay': None
            }
        }

        self.global_entries = {
            "Breath count": None, 
            "Profile delay (s)": None, 
            "Inhale delay (s)": None, 
            "Exhale delay (s)": None,
            }
        self.order = None

        fr_pad = tk.Frame(self.parent)
        fr_pad.grid(padx=10, pady=10, sticky=tk.NSEW)
        fr_pad.columnconfigure(0, weight=1)

        self.make_lobe_boxes(parent = fr_pad, lobes = self.lobes)
        self.make_maneuver_input(parent = fr_pad)
        self.hr(fr_pad)
        self.make_global_entries(parent = fr_pad)
        self.hr(fr_pad)
        self.make_lobe_entries(parent = fr_pad)
        self.hr(fr_pad)
        self.make_profile_input(parent = fr_pad)



    ###################
    # Utility functions
    ###################

    def get_lobes(self):
        return ''.join([str(self.lobes[lobe].get()) for lobe in self.lobes])

    ##################
    # Layout functions
    ##################

    def hr(self, parent):
        ttk.Separator(parent, orient='horizontal').grid(sticky=tk.EW)

    def make_lobe_boxes(self, parent, lobes):
        fr = tk.Frame(parent)
        fr.grid()
        tk.Label(fr, text="Position Tuning").grid(sticky=tk.W)

        fr_checks = tk.Frame(parent)
        fr_checks.grid()

        for index, lobe in enumerate(lobes):
            # fr_checks.columnconfigure(index, weight=1)
            lobes[lobe] = tk.IntVar()
            check = tk.Checkbutton(fr_checks, text = lobe, variable=lobes[lobe])
            check.grid(column=index, row = 0)

    def make_maneuver_input(self, parent):
        # maneuvers = ['Inhale', 'Exhale']

        fr_maneuver = tk.Frame(parent)
        fr_maneuver.grid()
        fr_maneuver.columnconfigure(0, weight=1)
        fr_maneuver.columnconfigure(1, weight=1)
        fr_maneuver.columnconfigure(2, weight=1)

        inhale_button = tk.Button(fr_maneuver, text = 'Inhale', command=lambda:self.perform_maneuver(maneuver = 'inhale'))
        exhale_button = tk.Button(fr_maneuver, text = 'Exhale', command=lambda:self.perform_maneuver(maneuver = 'exhale'))
        entry_steps = tk.Entry(fr_maneuver)
        self.entry_steps = entry_steps

        inhale_button.grid(row = 0, column=0)
        entry_steps.grid(row = 0, column=1, padx=10, pady=10)
        exhale_button.grid(row = 0, column=2)

    def make_global_entries(self, parent):
        frame = tk.Frame(parent)
        frame.grid(sticky=tk.EW)
        tk.Label(frame, text="Global settings").grid()
        frame.columnconfigure(0, weight=1)
        rows = 0

        frame_input = tk.Frame(frame)
        frame_input.grid(sticky=tk.EW)
        frame_input.columnconfigure(1,weight=1)

        for index, setting in enumerate(self.global_entries):
            label = tk.Label(frame_input, text=setting)
            label.grid(row = index, column=0, padx=5, pady=5, sticky=tk.W)

            entry = tk.Entry(frame_input)
            entry.grid(row=index, column=1, padx = 5, sticky=tk.EW)

            self.global_entries[setting] = entry

            rows+=1
        
        label = tk.Label(frame_input, text = "Order")
        label.grid(row=rows, column=0, sticky=tk.W, padx=5, pady=5)
        drop = ttk.Combobox(frame_input, values=('Exhale/Inhale', 'Inhale/Exhale'), state="readonly")
        drop.current(0)
        drop.grid(row=rows, column=1, sticky=tk.EW, padx=5, pady=5)
        self.order = drop

        button = tk.Button(frame, text = 'Update Global Settings', command=self.update_global_settings)
        button.grid(sticky=tk.EW, padx=5, pady=5, column=0)

    def make_lobe_entries(self, parent):
        frame = tk.Frame(parent)
        frame.grid(sticky=tk.EW)
        tk.Label(frame, text="Lobe settings").grid()
        frame.columnconfigure(0, weight=1)
        rows = 0

        frame_input = tk.Frame(frame)
        frame_input.grid(sticky=tk.EW)
        
        frame_input.columnconfigure(1,weight=1)
        frame_input.columnconfigure(2,weight=1)
        rows+=1
        tk.Label(frame_input, text="Lobe").grid(sticky=tk.EW, column=0, row=0)
        tk.Label(frame_input, text="Steps").grid(sticky=tk.EW, column=1, row=0)
        tk.Label(frame_input, text="Delay").grid(sticky=tk.EW, column=2, row=0)

        for index, lobe in enumerate(self.lobe_entries):
            label = tk.Label(frame_input, text=lobe)
            label.grid(row = index+1, column=0, padx=5, pady=5, sticky=tk.W)

            for i, setting in enumerate(self.lobe_entries[lobe]):
                entry = tk.Entry(frame_input)
                entry.grid(row=index+1, column=i+1, padx = 5, sticky=tk.EW)

                self.lobe_entries[lobe][setting] = entry

            rows+=1

        # print(self.lobe_entries)
        button = tk.Button(frame, text = 'Update Lobe Settings', command=self.update_lobe_settings)
        button.grid(sticky=tk.EW, padx=5, pady=5)


    def make_profile_input(self, parent):
        fr_breath_count = tk.Frame(parent)
        fr_breath_count.grid(sticky=tk.EW)
        fr_breath_count.columnconfigure(0, weight=1)

        button_check = tk.Button(fr_breath_count, text = 'Check Parameters', command = self.check_settings)
        button_check.grid(row = 0, padx=5, pady=5, sticky=tk.EW)

        button_run = tk.Button(fr_breath_count, text = 'Run', command = self.run, height=3)
        button_run.grid(row = 1, padx=5, pady=5, sticky=tk.EW)

    #########################
    # Action/Output functions
    #########################

    def perform_maneuver(self, maneuver):
        direction = 0
        if maneuver == 'inhale':
            direction = 1
        elif maneuver == 'exhale':
            direction = -1

        step_count = self.entry_steps.get()

        if step_count:
            try:
                step_count = abs(int(step_count))
                print(step_count, direction)
                Arduino.prepare_maneuver(self.ard, maneuver=maneuver, steps = step_count, motors = self.get_lobes())
                Arduino.run_maneuver(self.ard)
            except:
                print("Invalid input")

    def update_global_settings(self):
        if self.global_entries['Breath count'].get():
            Arduino.set_breath_count(self.ard, self.global_entries['Breath count'].get())
        if self.global_entries['Profile delay (s)'].get():
            Arduino.set_delay(self.ard, maneuver='profile', delay=self.global_entries['Profile delay (s)'].get())
        if self.global_entries['Inhale delay (s)'].get():
            Arduino.set_delay(self.ard, maneuver='inhale', delay=self.global_entries['Inhale delay (s)'].get())
        if self.global_entries['Exhale delay (s)'].get():
            Arduino.set_delay(self.ard, maneuver='exhale', delay=self.global_entries['Exhale delay (s)'].get())
        
        Arduino.set_maneuver_order(self.ard, maneuver= 'exhale' if self.order.current() == 0 else 'inhale')
        

    def update_lobe_settings(self):
        for index, lobe in enumerate(self.lobe_entries):
            selected_lobe = [0,0,0,0,0]
            selected_lobe[index] = 1
            selected_lobe = ''.join([str(_) for _ in selected_lobe])

            for setting, value in self.lobe_entries[lobe].items():
                if value.get():
                    Arduino.set_lobe_default(self.ard, setting, value.get(), selected_lobe)
        
        Arduino.update_lobe_delays(self.ard)

    def check_settings(self):
        print(Arduino.check_parameters(self.ard))

    def run(self):
        print(Arduino.check_parameters(self.ard))
        print(Arduino.check_lobe_delays(self.ard))
        Arduino.run_profile(self.ard)

if __name__ == "__main__":
    arduino = Arduino('/dev/ttyACM0')

    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    ManeuverPanel(frame, arduino_instance=arduino)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()