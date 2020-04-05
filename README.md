
# Topology optimization with ToOptix


<p align="center">
  <img src="https://github.com/DMST1990/ToOptixFreeCADAddon/blob/master/Images/StaticLoadCaseTwoRectangle.png" width="100%">
</p>


<p align="center">
  <img src="https://github.com/DMST1990/ToOptixFreeCADAddon/blob/master/Images/NoDesignSpace.png" width="100%">
</p>




## Current version
- Only 3D-FEM support
- Heat Transfer
- Static load case
- Material will change only in young module and conductivity
- Filter selects only the element around the filter object
- TESTED on VERSION 0.16 in FreeCAD Faild in Version >0.17

## Installation
- Install python 3.xx
- Download ToOptix

### General information
- Start this program in a user directory so Blender should be for example on the desktop 
- If you want to start Tooptix in "C:Programms\Blender Foundation ..." you need administrator rights (not reccomended)
- So i would suggest you should take a copy of blender and then use it on the desktop or some other user access folder
- (Optional) create a environment variable for Calculix (ccx)
- Test at first the two example files TwoRectanglesStruc.inp and TwoRectanglesTherm.inp

## For using the python FreeCAD Macro 
- This Macro is tested on FreeCAD 0.17. Later version might not work.
- You need to define a python3 path 'python3_path' in the file 'FreeCADMacro.py' because FreeCAD uses python2 as default
- You need to define a install path 'installation_path' in the file 'FreeCADMacro.py' that FreeCAD knows where ToOptix is located.
- During the macro FreeCAD changes the directory to the ToOptix folder and creates a 'config.json' file with the 'model.inp' path and the 'ccx.exe' path . 
- Create a FEM Model (which should work) for a static load case. Then run the Macro 'FreeCADMacro.py' in FreeCAD
- FreeCAD Macro, you can specifiy a non design material as well, just like before.
- Modification should be done in 'run_optimization_freeCAD.py'. This will be changed in the next version.

<p align="center">
  <img src="https://github.com/DMST1990/ToOptixFreeCADAddon/blob/master/Images/InstructionFreeCADMacro.png" width="100%">
</p>




```python, 

from run_optimization import run_optimization
import json
import os


json_path = 'config.json'
if __name__ == "__main__":
    # Optimization type --> seperated (combined is not implemented )
    cpus = 6
    opti_type = "seperated"
    sol_type = ["static"]
    with open(json_path, 'r') as file:
        data = json.load(file)
    files = [data['inp_path']]
    workDir = 'work'
    solverPath =  "\"" + str(data['ccx_path']) +  "\""
    inp_path = data['inp_path']
    files = [inp_path]
    for vol_frac in [0.4]:
        for penal in [3.0]:
            max_iteration = 100
            matSets = 20
            weight_factors = [1.0]
            no_design_set = 'SolidMaterial001Solid'
            no_design_set = None
            run_optimization(penal,  matSets, opti_type, sol_type,
                                                  weight_factors, max_iteration, vol_frac,
                                                  files, workDir, solverPath, cpus, no_design_set)
```

## Output
- STL File in a specific folder for every optimizaiton step
- Rendered Pictures of the result


