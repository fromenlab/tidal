# Influences:
# Matplotlib examples
# https://matplotlib.org/stable/users/explain/event_handling.html
# https://matplotlib.org/stable/users/explain/event_handling.html#event-attributes
# https://gist.github.com/astrojuanlu/7284462
# https://gist.github.com/YannDubs/8f5d0778fd6dda9b10140e735f373ce2


import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D

import numpy as np
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from api.bezier import *

from tkinter import filedialog
import json
   
class Interactor:
    """
    A polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """

    showverts = True
    epsilon = 0.1  # max pixel distance to count as a vertex hit
    click_epsilon = 10

    def __init__(self, ax, poly):
        # if poly.figure is None:
        #     raise RuntimeError('You must first add the polygon to a figure '
        #                        'or canvas before defining the interactor')
        self.bezier = None
        self.ax = ax
        canvas = poly.figure.canvas
        self.control_poly = poly

        # x, y = zip(*self.poly.xy)
        self.control_x = list(self.control_poly.get_xdata())
        self.control_y = list(self.control_poly.get_ydata())
        self.bezier_line = Line2D(self.control_x, self.control_y,
                        #    marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.bezier_line)

        self.cid = self.control_poly.add_callback(self.poly_changed)
        self._ind = None  # the active vert
        self._click = None # location of mouse click

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def on_draw(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.control_poly)
        self.ax.draw_artist(self.bezier_line)
        # do not need to blit here, this will fire before the screen is
        # updated

    def poly_changed(self, poly):
        """This method is called whenever the pathpatch object is called."""
        # only copy the artist props to the line (except visibility)
        vis = self.bezier_line.get_visible()
        Artist.update_from(self.bezier_line, poly)
        self.bezier_line.set_visible(vis)  # don't use the poly visibility state

    def get_ind_under_point(self, event):
        """
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """
        # display coords
        # xy = np.asarray(self.poly.xy)
        # xyt = self.poly.get_transform().transform(xy)
        # xt, yt = xyt[:, 0], xyt[:, 1]

        if not (self.control_x and self.control_y):
            ind = None
            return ind

        d = np.hypot(self.control_x - event.xdata, self.control_y - event.ydata)
        indseq, = np.nonzero(d == d.min())
        ind = indseq[0]

        if d[ind] >= self.epsilon:
            ind = None

        return ind

    def on_button_press(self, event):
        """Callback for mouse button presses."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)
        self._click = [event.x, event.y]

    def on_button_release(self, event):
        """Callback for mouse button releases."""
        if not self.showverts:
            return
        if event.button != 1:
            return

        if self._ind is None:
            d = np.hypot(self._click[0] - event.x, self._click[1] - event.y)
            if d < self.click_epsilon:
                self.control_x.append(event.xdata)
                self.control_y.append(event.ydata)
                self.update_bezier()

        self._ind = None

    def on_key_press(self, event):
        """Callback for key presses."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.control_poly.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.control_x.pop(ind)
                self.control_y.pop(ind)
                self.update_bezier()
        elif event.key == 'i':
            self.control_x.append(event.xdata)
            self.control_y.append(event.ydata)
            self.order_points()
            self.update_bezier()
        if self.bezier_line.stale:
            self.canvas.draw_idle()

    def on_mouse_move(self, event):
        """Callback for mouse movements."""
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return

        self.control_x[self._ind] = event.xdata
        self.control_y[self._ind] = event.ydata
        self.update_bezier()

    def order_points(self):
        self.control_x, self.control_y = [list(_) for _ in zip(*sorted(zip(self.control_x, self.control_y)))]
        self.update_bezier()

    def flip_points(self):
        self.control_x = [((0.5-x)+0.5) for x in self.control_x]
        self.update_bezier()
            
    def build_bezier(self, n = 200):
        self.bezier = Bezier(self.control_x, self.control_y)
        x, y = self.bezier.get_curve_coords(n)
        return x, y

    def update_bezier(self):
        self.control_poly.set_data(self.control_x, self.control_y)
        self.bezier_line.set_data(*self.build_bezier())
        self.canvas.draw()

class BezierPanel:
    def __init__(self, parent, plot_title = '') -> None:
        self.parent = parent
        self.plot_title = plot_title

        fr = parent
        # fr = tk.Frame(parent)
        # fr.grid(column=0, row = 0)

        canvas = self.make_canvas(fr)

        # pack_toolbar=False will make it easier to use a layout manager later on.
        toolbar = NavigationToolbar2Tk(canvas, fr, pack_toolbar=False)
        toolbar.update()

        # canvas.mpl_connect(
        #     "key_press_event", lambda event: print(f"you pressed {event.key}"))
        canvas.mpl_connect("key_press_event", key_press_handler)

        # Packing order is important. Widgets are processed sequentially and if there
        # is no space left, because the window is too small, they are not displayed.
        # The canvas is rather flexible in its size, so we pack it last which makes
        # sure the UI controls are displayed as long as possible.
        # button_quit.pack(side=tk.BOTTOM)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        fr_button = tk.Frame(fr)
        fr_button.columnconfigure(0, weight=1)
        fr_button.columnconfigure(1, weight=1)
        fr_button.columnconfigure(2, weight=1)
        fr_button.columnconfigure(3, weight=1)

        button_log = tk.Button(fr_button, text="Log", command = self.log_points)
        button_reset = tk.Button(fr_button, text="Reset", command = self.reset_points)
        button_order = tk.Button(fr_button, text="Order", command = self.order_points)
        button_flip = tk.Button(fr_button, text="Flip", command = self.flip_points)
        button_save = tk.Button(fr_button, text="Save", command = self.save_points)
        button_load = tk.Button(fr_button, text="Load", command = self.load_points)

        button_load.pack(padx=5, side = tk.LEFT)
        button_log.pack(padx=5, side = tk.LEFT)
        button_order.pack(padx=5, side = tk.LEFT)
        button_flip.pack(padx=5, side = tk.LEFT)
        button_save.pack(padx=5, side = tk.LEFT)
        button_reset.pack(padx=5, side = tk.LEFT)
        

        fr_button.pack(fill='x', pady=10)
    
    def make_canvas(self, parent):
        fig = Figure()
        ax = fig.subplots()
        
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()

        # ax.set_title('Click and drag a point to move it')
        ax.set_title(self.plot_title)
        ax.set_xlabel('Maneuver progress')
        ax.set_ylabel('Relative speed')
        ax.set_xlim((-0.1, 1.1))
        ax.set_ylim((-0.1, 1.1))

        line = Line2D([], [], ls='--', c='#666666',
                  marker='x', mew=2, mec='#204a87')
        ax.add_line(line)

        self.interactor = Interactor(ax, line)

        return canvas
    
    def log_points(self):
        print(f"Control points (x): {self.interactor.control_x}")
        print(f"Control points (y): {self.interactor.control_y}")

    def reset_points(self):
        self.interactor.control_x = [0]
        self.interactor.control_y = [0]
        self.interactor.update_bezier()

    def order_points(self):
        self.interactor.order_points()

    def flip_points(self):
        self.interactor.flip_points()

    def save_points(self):
        points = {'x': self.interactor.control_x, 'y': self.interactor.control_y}
        with filedialog.asksaveasfile(defaultextension=".cp", filetypes=[('Control Points','*.cp'), ('All files', '*.*')]) as f:
            json.dump(points, f, indent=4)
            print(f"Control points saved at: {f.name}")

    def load_points(self):
        with filedialog.askopenfile(defaultextension=".cp", filetypes=[('Control Points','*.cp'), ('All files', '*.*')]) as f:
            points = json.load(f)
            self.interactor.control_x = points['x']
            self.interactor.control_y = points['y']
            self.interactor.update_bezier()
            print(f"Control points loaded from: {f.name}")

class BezierGuide():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.instructions = tk.Label(parent, font=("SansSerif", 12), justify = tk.LEFT)
        contents = tk.StringVar()
        self.instructions['textvariable'] = contents
        
        lines = [
            '- Click within a plot to add a control point.',
            '- Click and drag to move control points.',
            '- To use hotkeys, click a plot title. Then move the mouse to the plot area, and press the key:',
            '      (t)   Toggle point visibility',
            '      (i)   Insert a control point at the mouse position',
            '      (d) Delete the control point at the mouse position'
        ]

        contents.set('\n'.join(lines))

    def pack(self, *args, **kwargs):
        self.instructions.pack(*args, **kwargs)
        
if __name__ == "__main__":
    root = tk.Tk()

    fr = tk.Frame(root)
    fr.pack(expand=True, fill='both')

    BezierGuide(fr).pack(anchor=tk.W)   
    BezierPanel(fr, plot_title="Control curve")

    root.mainloop()

        