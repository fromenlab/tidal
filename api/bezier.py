import numpy as np

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
        self.control_points = [Point(coord[0], coord[1]) for coord in zip(x,y)]
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