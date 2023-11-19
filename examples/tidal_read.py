import os
import json

# %%
f = open('config.tidal', 'r')
d = json.load(f)

# %%
d.items()

# %%
d['lobes']

# %%
d['lobes'][0]

# %%
d['lobes']['RU'] # does not work

# %%
d['lobes'][0]['step_delay_constant']

# %%
d['lobes'][0]['inhale_control_points']

# %%
d['lobes'][0]['inhale_control_points']['x']
d['lobes'][0]['inhale_control_points']['y']