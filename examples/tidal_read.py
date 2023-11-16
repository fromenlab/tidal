import os
import json

# %%
f = open('examples/tidal.json', 'r')
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
d['lobes'][0]['profile_delay']

# %%
d['lobes'][0]['profile_delay'][-1]

# %%
d['lobes'][0]['profile_delay'][1]

# %%
d['lobes'][0]['profile_delay'][0]['control_points']

# %%
d['lobes'][0]['profile_delay'][0]['control_points'] = [1,2,5]

# %%
d['lobes'][0]['profile_delay'][0]['control_points']


