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

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point object@({self.x},{self.y})"
    
    def get_coords(self):
        return self.x, self.y
    
class Bezier:
    def __init__(self, x, y) -> None:
        self.control_points = [Point(point[0], point[1]) for point in zip(x,y)]
        pass  

    def get_point_at_parameter(self, points: Point, t) -> Point:
        if len(points) == 1:
            return points[0]
        else:
            recursed_points = []
            for current, next in zip(points, points[1:]):
                x = (1-t) * current.x + t * next.x
                y = (1-t) * current.y + t * next.y
                recursed_points.append(Point(x,y))
            return self.get_point_at_parameter(recursed_points, t)
        
    def get_curve_coords(self, n):
        curve_points = []  
        for k in range(n):
            t = float(k) / (n - 1)
            curve_points.append(self.get_point_at_parameter(self.control_points, t))

        x, y = np.column_stack([point.get_coords() for point in curve_points])

        return x, y


    
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

    def __init__(self, ax, poly):
        # if poly.figure is None:
        #     raise RuntimeError('You must first add the polygon to a figure '
        #                        'or canvas before defining the interactor')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        # x, y = zip(*self.poly.xy)
        self.x = list(self.poly.get_xdata())
        self.y = list(self.poly.get_ydata())
        self.line = Line2D(self.x, self.y,
                        #    marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # the active vert

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def on_draw(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        # do not need to blit here, this will fire before the screen is
        # updated

    def poly_changed(self, poly):
        """This method is called whenever the pathpatch object is called."""
        # only copy the artist props to the line (except visibility)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # don't use the poly visibility state

    def get_ind_under_point(self, event):
        """
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """
        # display coords
        # xy = np.asarray(self.poly.xy)
        # xyt = self.poly.get_transform().transform(xy)
        # xt, yt = xyt[:, 0], xyt[:, 1]

        if not (self.x and self.y):
            ind = None
            return ind

        d = np.hypot(self.x - event.xdata, self.y - event.ydata)
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

        if self._ind is None:
            self.x.append(event.xdata)
            self.y.append(event.ydata)
            self.update_bezier()

    def on_button_release(self, event):
        """Callback for mouse button releases."""
        if not self.showverts:
            return
        if event.button != 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback for key presses."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.x.pop(ind)
                self.y.pop(ind)
                self.update_bezier()
                # self.poly.xy = np.delete(self.poly.xy,
                #                          ind, axis=0)
                # self.line.set_data(zip(*self.poly.xy))
        elif event.key == 'i':
            self.x.append(event.xdata)
            self.y.append(event.ydata)
            self.update_bezier()
        if self.line.stale:
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

        self.x[self._ind] = event.xdata
        self.y[self._ind] = event.ydata
        self.update_bezier()
            
    def build_bezier(self):
        self.bezier = Bezier(self.x, self.y)
        x, y = self.bezier.get_curve_coords(200)
        return x, y

    def update_bezier(self):
        self.poly.set_data(self.x, self.y)
        self.line.set_data(*self.build_bezier())
        self.canvas.draw()

class BezierPanel:
    def __init__(self, parent) -> None:
        self.parent = parent

        fr = parent
        # fr = tk.Frame(parent)
        # fr.grid(column=0, row = 0)

        canvas = self.make_canvas(fr)

        # pack_toolbar=False will make it easier to use a layout manager later on.
        toolbar = NavigationToolbar2Tk(canvas, fr, pack_toolbar=False)
        toolbar.update()

        canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
        canvas.mpl_connect("key_press_event", key_press_handler)

        button_quit = tk.Button(fr, text="Quit", command=fr.destroy)

        # Packing order is important. Widgets are processed sequentially and if there
        # is no space left, because the window is too small, they are not displayed.
        # The canvas is rather flexible in its size, so we pack it last which makes
        # sure the UI controls are displayed as long as possible.
        # button_quit.pack(side=tk.BOTTOM)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def make_canvas(self, parent):
        fig = Figure()
        ax = fig.subplots()
        
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()

        ax.set_title('Click and drag a point to move it')
        ax.set_xlim((-0.1, 1.1))
        ax.set_ylim((-0.1, 1.1))

        line = Line2D([], [], ls='--', c='#666666',
                  marker='x', mew=2, mec='#204a87')
        ax.add_line(line)

        Interactor(ax, line)

        return canvas
        
if __name__ == "__main__":
    root = tk.Tk()

    BezierPanel(root)

    root.mainloop()

        