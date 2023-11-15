import tkinter as tk
import pandas as pd
import glob
from tkinter import filedialog

class PlotPanel:
    def __init__(self, parent):
        self.parent = parent

        fr_pad = tk.Frame(self.parent)
        fr_pad.grid(padx=10, pady=10, sticky=tk.NSEW)
        fr_pad.columnconfigure(0, weight=1)

        self.entry_input = self.make_path_entry(fr_pad)
        self.make_run_frame(fr_pad)

    def make_path_entry(self, parent):
            # Set frames for layout
        frame_paths = tk.Frame(parent)
        frame_paths.grid(sticky = tk.EW)
        frame_paths.columnconfigure(1, weight=1)

        button_input = tk.Button(frame_paths, text = 'Data Folder', command = lambda:self.select_folder(entry_input))
        button_input.grid(row = 0, column = 0, padx=5, sticky=tk.EW)
        entry_input = tk.Entry(frame_paths)
        entry_input.grid(row=0, column=1, padx = 5, sticky=tk.EW)

        return entry_input

    def select_folder(self, entry):
        folder_path = filedialog.askdirectory()
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        self.data_path = folder_path

    def make_run_frame(self, parent):

        frame_run = tk.Frame(parent)
        frame_run.grid(sticky=tk.EW, column=0, row=1)
        frame_run.columnconfigure(0, weight=1)

        # Run options
        button_run = tk.Button(frame_run, text = 'Make Plot', command = lambda:self.run(), padx=10, pady=10)
        button_run.grid(column=0, row = 0, padx=10, pady=10, sticky=tk.EW)

    def run(self):
        print(self.data_path)
        df = pd.concat(
        [
            pd.read_csv(filename).assign(source=filename)[["0", "source"]] for filename in sorted(glob.glob(fr'{self.data_path}/*.csv'))
        ], 
        ignore_index=True
        )

        df.plot(y='0')

        pd.options.plotting.backend = "plotly"

        fig = df.plot(y='0')
        fig.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    PlotPanel(frame)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()