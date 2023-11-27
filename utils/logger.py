from datetime import datetime
import tkinter as tk
import os

class Logger():
    def __init__(self, console_output: tk.Text = None, file_output = None):
        self.console_output = console_output
        self.file_output = file_output

    def set_file_output(self, path):
        self.file_output = path

    def set_console_output(self, object):
        self.console_output = object
    
    def write(self, string):
        if self.console_output:
            self.console_output.configure(state = 'normal')
            self.console_output.insert(tk.END, string)
            self.console_output.configure(state = 'disabled')
            self.console_output.see('end')
            self.console_output.update_idletasks()
        
        if self.file_output:
            # TODO: Decide whether to pass file name or directory, how to make modular
            write_log(dir = os.path.dirname(self.file_output), lines = [string])
            # with open(self.file_output, 'a', encoding='utf-8') as f:
            #     for line in string:
            #         f.writelines(line)

    def flush(self):
        pass

def write_log(dir, name = "log.txt", lines = None):
    if lines == ["\n"]:
        return

    if (not os.path.exists(dir)):
        os.makedirs(dir)

    log_path = os.path.join(dir, name)

    if (not os.path.exists(log_path)):
         mode = 'w'
    else:
         mode = 'a'

    with open(log_path, mode, encoding='utf-8') as f:
        f.writelines(["---", "\n", datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), "\n"])

        for line in lines:
            f.writelines([line, "\n"])

        f.writelines(["\n", "\n"])
