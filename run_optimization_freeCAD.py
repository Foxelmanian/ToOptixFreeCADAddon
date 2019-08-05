

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
    if os.path.exists(json_path):
        os.remove(json_path)

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
            run_optimization(penal,  matSets, opti_type, sol_type,
                                                  weight_factors, max_iteration, vol_frac,
                                                  files, workDir, solverPath, cpus, no_design_set)