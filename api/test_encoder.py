import json
from api.lobe import Lobe
from api.TIDAL import TIDAL
from api.TIDAL import TIDALEncoder
lobe = Lobe("RU")
print(json.dumps(lobe, indent = 4, cls = TIDALEncoder))

tidal = TIDAL()
TIDALEncoder().encode(tidal.lobes)
print(json.dumps(tidal, indent = 4, cls = TIDALEncoder))

tidal.substitute_params()