# -*- coding: utf-8 -*-


import sys
import os
import subprocess
import json

python3_path = # Enter python path
installation_path = # Enter addon path

import FreeCAD
import Part
import commands
import FemGui
import ObjectsFem
import Fem
import FemGui
from femtools import ccxtools

fea = ccxtools.FemToolsCcx()
fea.update_objects()
message = fea.check_prerequisites()
if not message:
    fea.write_inp_file()
    ccx_path = fea.__dict__['ccx_binary']
    inp_path = fea.__dict__['inp_file_name']

else:
    raise IOError


# Global settings for the installation script
# Use python 3 for executing the tooptix script
ccx_path = str(ccx_path)
ccx_path.replace("/", "\\")
run_path = os.path.join("run_optimization_freeCAD.py")
data = {'ccx_path': ccx_path,
        'inp_path': inp_path}
with open(os.path.join(installation_path, 'config.json'), 'w') as file:
    json.dump(data, file)

os.chdir(installation_path)
command = python3_path + ' ' + run_path
subprocess.Popen(command)




