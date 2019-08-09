#!/usr/bin/env/python

import os

from PySide import QtGui

import FreeCAD
import FreeCADGui

from femtools import ccxtools
from ToOptixCore.TopologyOptimizer.OptimizationController import OptimizationController

Msg = FreeCAD.Console.PrintMessage
Log = FreeCAD.Console.PrintLog
Err = FreeCAD.Console.PrintError


class PerformToOptixCommand:
    "Performs ToOptix topology optimization"

    def GetResources(self):
        return {"MenuText": "Topology Optimization",
                "Accel": "",
                "ToolTip": "Performs topology optimization",
                "Pixmap": ":/icons/to.svg"
                }

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            try:
                ccxtools.FemToolsCcx()
            except Exception:
                return False
            else:
                return True

    def Activated(self):
        fea = ccxtools.FemToolsCcx()
        fea.update_objects()
        message = fea.check_prerequisites()
        Log(message)

        fea.write_inp_file()
        ccx_path = fea.__dict__['ccx_binary']
        inp_path = fea.__dict__['inp_file_name']
        for (key, val) in fea.__dict__.items():
            Log(key + ": " + str(val) + "\n")
        Log(inp_path)

        cpus = 3
        files = [inp_path]
        sol_type = ["static"]
        opti_type = "seperated"
        max_iterations = 100
        penal = 3.0
        vol_frac = 0.4
        matSets = 20
        weight_factors = [1.0]
        workDir = "/home/joha2/topopttest/"
        solverPath = "/usr/bin/ccx"
        no_design_set = "SolidMaterial001Solid"

        os.environ['OMP_NUM_THREADS'] = str(cpus)
        opti_controller = OptimizationController(files,
                                                 sol_type,
                                                 reverse=False,
                                                 type=opti_type)
        opti_controller.set_maximum_iterations(max_iterations)
        opti_controller.set_penalty_exponent(penal)
        opti_controller.set_number_of_material_sets(matSets)
        opti_controller.set_solver_path(solverPath)
        opti_controller.set_weight_factors(weight_factors)
        opti_controller.plot_only_last_result(False)

        # Start the optimization
        opti_controller.set_result_file_name('stl_result' +
                                             str(vol_frac) + "__")
        opti_controller.set_result_path(workDir)
        opti_controller.set_volumina_ratio(vol_frac)
        opti_controller.set_no_design_element_set(no_design_set)
        opti_controller.run()


FreeCADGui.addCommand('PerformToOptixCommand', PerformToOptixCommand())
