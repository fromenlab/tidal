import numpy as np
import json

class Lobe():
    def __init__(self, name) -> None:
        self._name = name # indicating that _name is not public

        # Constant delay profile and position tuning
        self._gui_checkbox = None
        self._gui_constant_step_entry = None
        self._gui_constant_delay_entry = None
        
        self._step_count_constant = 200
        self._step_delay_constant = 2100
        

        # Variable delay profile
        # Moving away from properties for certain variables, for expedience
        # Revisit in the future

        # Default values
        self._step_count_variable = 200
        self._imin = 300
        self._emin = 300
        self._imax = 3000
        self._emax = 3000
        self._inhale_control_points = []
        self._inhale_delays = []
        self._exhale_control_points = []
        self._exhale_delays = []

        # UI components
        self.gui_variable_step_entry = None

        self.gui_variable_inhale_min_delay_entry = None
        self.gui_variable_inhale_max_delay_entry = None

        self.gui_variable_exhale_min_delay_entry = None
        self.gui_variable_exhale_max_delay_entry = None

        self._gui_inhale_bezier = None
        self._gui_exhale_bezier = None
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gui_checkbox(self):
        return self._gui_checkbox
    
    @gui_checkbox.setter
    def gui_checkbox(self, value):
        self._gui_checkbox = value

    @property   
    def gui_constant_step_entry(self):
        return self._gui_constant_step_entry
    
    @gui_constant_step_entry.setter
    def gui_constant_step_entry(self, value):
        self._gui_constant_step_entry = value

    @property
    def gui_constant_delay_entry(self):
        return self._gui_constant_delay_entry
    
    @gui_constant_delay_entry.setter
    def gui_constant_delay_entry(self, value):
        self._gui_constant_delay_entry = value

    @property
    def gui_inhale_bezier(self):
        return self._gui_inhale_bezier
    
    @gui_inhale_bezier.setter
    def gui_inhale_bezier(self, value):
        self._gui_inhale_bezier = value

    @property
    def gui_exhale_bezier(self):
        return self._gui_exhale_bezier
    
    @gui_exhale_bezier.setter
    def gui_exhale_bezier(self, value):
        self._gui_exhale_bezier = value

    @property
    def step_count_constant(self):
        return self._step_count_constant
    
    @step_count_constant.setter
    def step_count_constant(self, value):
        self._step_count_constant = value

    @property
    def step_delay_constant(self):
        return self._step_delay_constant
    
    @step_delay_constant.setter
    def step_delay_constant(self, value):
        if value != '':
            self._step_delay_constant = value

    @property
    def inhale_control_points(self):
        return self._inhale_control_points
    
    @inhale_control_points.setter
    def inhale_control_points(self, value):
        self._inhale_control_points = value

    @property
    def inhale_delays(self):
        return self._inhale_delays
    
    @inhale_delays.setter
    def inhale_delays(self, value):
        self._inhale_delays = value

    @property
    def inhale_delays_formatted(self):
        s = f"{[x for x in self.inhale_delays]}".strip('[]')
        s = f"{{{s}}}"
        return s

    @property
    def exhale_control_points(self):
        return self._exhale_control_points
    
    @exhale_control_points.setter
    def exhale_control_points(self, value):
        self._exhale_control_points = value

    @property
    def exhale_delays(self):
        return self._exhale_delays
    
    @exhale_delays.setter
    def exhale_delays(self, value):
        self._exhale_delays = value

    @property
    def exhale_delays_formatted(self):
        s = f"{[x for x in self.exhale_delays]}".strip('[]')
        s = f"{{{s}}}"
        return s

    @property
    def imin(self):
        return self._imin
    
    @imin.setter
    def imin(self, value):
        if value != '':
            self._imin = int(value)

    @property
    def imax(self):
        return self._imax
    
    @imax.setter
    def imax(self, value):
        if value != '':
            self._imax = int(value)

    @property
    def emin(self):
        return self._emin
    
    @emin.setter
    def emin(self, value):
        if value != '':
            self._emin = int(value)

    @property
    def emax(self):
        return self._emax
    
    @emax.setter
    def emax(self, value):
        if value != '':
            self._emax = int(value)

    @property
    def step_count_variable(self):
        return self._step_count_variable
    
    @step_count_variable.setter
    def step_count_variable(self, value):
        if value != '':
            self._step_count_variable = int(value)
    

    def update_variable_profile_params(self):
        self.step_count_variable = self.gui_variable_step_entry.get()
        self.imin = self.gui_variable_inhale_min_delay_entry.get()
        self.imax = self.gui_variable_inhale_max_delay_entry.get()
        self.emin = self.gui_variable_exhale_min_delay_entry.get()
        self.emax = self.gui_variable_exhale_max_delay_entry.get()
        
        inhale_interactor = self.gui_inhale_bezier.interactor
        self.inhale_control_points = {'x': inhale_interactor.control_x, 'y': inhale_interactor.control_y}

        exhale_interactor = self.gui_exhale_bezier.interactor
        self.exhale_control_points = {'x': exhale_interactor.control_x, 'y': exhale_interactor.control_y}
        
        self.calculate_relative_flow_delays()

    def calculate_relative_flow_delays(self):
        ibezier = self.gui_inhale_bezier.interactor.bezier
        ebezier = self.gui_exhale_bezier.interactor.bezier
        if not (ibezier and ebezier):
            print(f"Both profiles must be supplied for the lobe: {self.name}. Cancelling update.")
            return
        # Get relative flow values equally-spaced along x range
        xi, yi = ibezier.get_interval_coords(self.step_count_variable)
        xe, ye = ebezier.get_interval_coords(self.step_count_variable)
        
        # Convert min delays to relative flow rates
        # Note terminology reversal -- min delay corresponds to max flow
        # Note that this is also depended on lobe shape, etc
        imaxf = 1/self.imin
        iminf = 1/self.imax
        emaxf = 1/self.emin
        eminf = 1/self.emax

        # Interpolate Bezier values - map to inverse delays
        yi_mapped = np.interp(yi, (0,1), (iminf, imaxf))
        ye_mapped = np.interp(ye, (0,1), (eminf, emaxf))

        # Convert to delays and cast as integer values with numpy
        self.inhale_delays = (1/yi_mapped).astype(int)
        self.exhale_delays = (1/ye_mapped).astype(int)
