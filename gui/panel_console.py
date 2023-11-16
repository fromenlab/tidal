import tkinter as tk
from tkinter import scrolledtext
import sys
import os
from api.TIDAL import TIDAL

class Logger():
    def __init__(self, console_output = None, file_output = None):
        self.console_output = console_output
        self.file_output = file_output

    def set_file_output(self, path):
        self.file_output = path

    def set_console_output(self, object):
        self.console_output = object
    
    def write(self, string):
        self.console_output.configure(state = 'normal')
        self.console_output.insert(tk.END, string)
        self.console_output.configure(state = 'disabled')
        self.console_output.see('end')

        with open(self.file_output, 'a', encoding='utf-8') as f:
            for line in string:
                f.writelines(line)

    def flush(self):
        pass

class LogPanel():
    def __init__(self, parent, tidal_instance: TIDAL = None) -> None:
        self.parent = parent
        self.tidal_instance = tidal_instance
        self.logger = Logger()

        self.make_console_view(parent)

    def get_logger(self):
        return self.logger
    
    def set_logger(self, logger):
        self.logger = logger

    def make_console_view(self, parent):
        console_view = scrolledtext.ScrolledText(parent, height=5)
        console_view.configure(state = 'disabled')
        # console_view.grid(padx=5, pady=5, sticky=tk.NSEW)
        console_view.pack(fill='both', expand=True)

        self.logger.set_console_output(console_view)

        if self.tidal_instance is None:
            self.logger.set_file_output(os.path.join(r'out.log'))
        else:
            # self.logger.set_file_output(self.tidal_instance.get_log)
            pass

        sys.stdout = self.logger

if __name__ == "__main__":

    def print_range():
        for _ in range(10):
            print(f"The next number is {_}")

    root = tk.Tk()

    button = tk.Button(root, text = 'Print', command=print_range)

    fr_panel = tk.Frame(root)
    fr_panel.columnconfigure(0,weight=1)
    fr_panel.rowconfigure(0,weight=1)
    LogPanel(fr_panel)

    button.pack(fill='x')
    fr_panel.pack(expand=True, fill='both')

    root.mainloop()