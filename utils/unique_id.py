import os
from datetime import datetime
import hashlib

def make_id(properties):
    properties_string = ','.join(map(str, properties))
    properties_fragment = (hashlib.md5(properties_string.encode("UTF-8")).hexdigest())[:3]

    date_info = datetime.now().strftime("%y%m%d")
    date_utc = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    instance_fragment = (hashlib.sha256(date_utc.encode("UTF-8")).hexdigest())[:2]

    unique_id = '-'.join([date_info, properties_fragment, instance_fragment])
    
    return unique_id, date_utc

def make_run_folder(output_dir, id):
    if (not os.path.exists(output_dir)):
            os.mkdir(output_dir)
    
    run_folder = os.path.join(output_dir, id)
    data_folder = os.path.join(run_folder, "data")
    if (not os.path.exists(run_folder)):
            os.mkdir(run_folder)
            os.mkdir(data_folder)

    return run_folder, data_folder

