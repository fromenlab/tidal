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
        self.gui_variable_step_entry = None
        self.step_count_variable = 200

        self.gui_variable_inhale_min_delay_entry = None
        self.gui_variable_inhale_max_delay_entry = None

        self.gui_variable_exhale_min_delay_entry = None
        self.gui_variable_exhale_max_delay_entry = None

        self._gui_inhale_bezier = None
        self._inhale_control_points = []
        self._inhale_delays = []

        self._gui_exhale_bezier = None
        self._exhale_control_points = []
        self._exhale_delays = []

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