import tkinter as tk
from tkinter import scrolledtext
import sys
import os
from api.TIDAL import TIDAL
from utils.logger import Logger

class LogPanel():
    def __init__(self, parent, tidal_instance: TIDAL = None) -> None:
        self.parent = parent
        self.tidal_instance = tidal_instance
        self._logger = Logger()

        self.make_console_view(parent)

    @property
    def logger(self):
        return self._logger
    
    @logger.setter
    def name(self, value):
        self._logger = value

    def make_console_view(self, parent):
        console_view = scrolledtext.ScrolledText(parent, height=5)
        console_view.configure(state = 'disabled')
        # console_view.grid(padx=5, pady=5, sticky=tk.NSEW)
        console_view.pack(fill='both', expand=True)

        self.logger.set_console_output(console_view)

        sys.stdout = self.logger
        self.tidal_instance.logger = self.logger

if __name__ == "__main__":

    def print_range():
        for _ in range(10):
            print(f"The next number is {_}")

    root = tk.Tk()

    button = tk.Button(root, text = 'Print', command=print_range)

    fr_panel = tk.Frame(root)
    fr_panel.columnconfigure(0,weight=1)
    fr_panel.rowconfigure(0,weight=1)
    LogPanel(fr_panel, TIDAL())

    button.pack(fill='x')
    fr_panel.pack(expand=True, fill='both')

    root.mainloop()