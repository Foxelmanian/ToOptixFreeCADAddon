## BLENDER from .TopologyOptimizer.OptimizationController import OptimizationController
## PYCHARM from TopologyOptimizer.OptimizationController import OptimizationController
from ToOptixCore.TopologyOptimizer.OptimizationController import OptimizationController
import os
from enum import Enum

def run_optimization(penal,  matSets, opti_type, sol_type,
                    weight_factors, max_iteration, vol_frac,
                    files, workDir, solverPath, cpus, no_design_set=None):
    print('Start topology otpimization')

    os.environ['OMP_NUM_THREADS'] = str(cpus)
    opti_controller = OptimizationController(files, sol_type, reverse=False, type=opti_type)
    opti_controller.set_maximum_iterations(max_iteration)
    opti_controller.set_penalty_exponent(penal)
    opti_controller.set_number_of_material_sets(matSets)
    opti_controller.set_solver_path(solverPath)
    opti_controller.set_weight_factors(weight_factors)
    opti_controller.plot_only_last_result(False)

    # Start the optimization
    opti_controller.set_result_file_name('stl_result' + str(vol_frac) + "__")
    opti_controller.set_result_path(workDir)
    opti_controller.set_volumina_ratio(vol_frac)
    opti_controller.set_no_design_element_set(no_design_set)
    opti_controller.run()



if __name__ == "__main__":
    # Optimization type --> seperated (combined is not implemented )
    cpus = 6
    opti_type = "seperated"
    sol_type = ["heat", "static"]

    files = ['TwoRectanglesTherm.inp', "TwoRectanglesStruc.inp"]
    workDir = 'work'
    solverPath = 'ccx'
    vol_frac = 0.3
    penal = 2.4
    max_iteration = 40
    matSets = 10
    weight_factors = [1.0, 1.0]
    no_design_set = None
    run_optimization(penal,  matSets, opti_type, sol_type,
                                          weight_factors, max_iteration, vol_frac,
                                          files, workDir, solverPath, cpus, no_design_set)
