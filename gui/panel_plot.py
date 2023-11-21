import tkinter as tk
import pandas as pd
import glob
from tkinter import filedialog

# Can be run as standalone interface
class PlotPanel:
    def __init__(self, parent):
        self.parent = parent
        self.plot_process = None

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
        button_run = tk.Button(frame_run, text = 'Make Interactive Plot', command = lambda:self.run(), padx=10, pady=10)
        button_run.grid(column=0, row = 0, padx=10, pady=10, sticky=tk.EW)
        button_stop = tk.Button(frame_run, text = 'Stop Server', command = lambda:self.terminate_plot(), padx=10, pady=10)
        button_stop.grid(column=1, row = 0, padx=10, pady=10, sticky=tk.EW)

    def run(self):
        print(self.data_path)
        df = pd.concat(
        [
            pd.read_csv(filename).assign(source=filename)[["0", "source"]] for filename in sorted(glob.glob(fr'{self.data_path}/*.csv'))
        ], 
        ignore_index=True
        )

        # df.plot(y='0')

        df['time_s'] = df.index*(10/1000) # hard-coded sample rate at 10ms
        # df.columns # to display column names

        pd.options.plotting.backend = "plotly"

        fig = df.plot.line(x='time_s',y='0', markers=True)
        fig.update_layout(
            xaxis_title = "Time (s)",
            yaxis_title = "Flow rate (SLPM)"
        )

        # fig.show()

        import json
        from dash import Dash, dcc, html, Input, Output, callback
        import numpy as np

        app = Dash()

        app.layout = html.Div([
            dcc.Graph(figure=fig, id = 'fig'),
            html.Div([
                html.B("Time (s): "),
                html.Div(id='out-time')
            ]),
            html.Div([
                html.B("Volume (L): "),
                html.Div(id='out-vol')
            ]),
            html.Div([
                html.B("Peak flow rate (SLPM): "),
                html.Div(id='out-flow-peak')
            ]),
            html.Div([
                html.B("Mean flow rate (SLPM): "),
                html.Div(id='out-flow-mean')
            ]),
            html.Div([
                html.B("Median flow rate (SLPM): "),
                html.Div(id='out-flow-median')
            ])
        ])

        @callback(
            Output('out-time', 'children'),
            Output('out-vol', 'children'),
            Output('out-flow-peak', 'children'),
            Output('out-flow-mean', 'children'),
            Output('out-flow-median', 'children'),
            Input('fig', 'selectedData'))
        def display_integral(selectedData):
            if selectedData is not None:
                # print(json.dumps(selectedData, indent=4))
                df_select = pd.DataFrame({'x' : [point['x'] for point in selectedData['points']], 
                                          'y' : [point['y'] for point in selectedData['points']]})
                
                integral_area = np.trapz(y = df_select['y'], x = df_select['x'])
                volume_L = integral_area/60 # conversion from SLPM to SL/sec
                time_s = np.max(df_select['x']) - np.min(df_select['x'])
                flow_peak_slpm = np.max(df_select['y'])
                flow_average_slpm = np.mean(df_select['y'])
                flow_median_slpm = np.median(df_select['y'])

                outputs = [round(time_s, 3), 
                           round(volume_L, 3), 
                           round(flow_peak_slpm, 3), 
                           round(flow_average_slpm, 3), 
                           round(flow_median_slpm, 3)]

                return outputs
            else:
                return '','','','',''

        from multiprocessing import Process
        self.plot_process = Process(target=lambda: app.run_server(debug=True, use_reloader = False))
        self.plot_process.start()
        import webbrowser
        webbrowser.open_new("http://localhost:8050/")

    def terminate_plot(self):
        if self.plot_process is not None:
            try:
                self.plot_process.terminate()
            except:
                print("There was an error stopping the process")
            else:
                print("Interactive plot process closed")


if __name__ == "__main__":
    root = tk.Tk()
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, width=100, height=100)
    frame.columnconfigure(0, weight=1)
    PlotPanel(frame)
    frame.grid(padx=10, pady=10, sticky=tk.NSEW, column=0, row=0)

    root.mainloop()