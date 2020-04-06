#!/usr/bin/env/python

from PySide import QtGui

import FreeCAD
import FreeCADGui

from femtools import ccxtools
from .TaskPanel_ToOptix_Start import TaskPanelToOptixStart


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
        fea.setup_working_dir()  # sets up fea.working_dir
        fea.setup_ccx()  # sets up fea.ccx_binary
        message = fea.check_prerequisites()

        # setup start parameters for optimization
        preferences = {}
        preferences["ccx_binary_path"] = fea.ccx_binary
        preferences["working_directory"] = fea.working_dir

        taskpanel = TaskPanelToOptixStart(fea, message, preferences)
        FreeCADGui.Control.showDialog(taskpanel)


FreeCADGui.addCommand('PerformToOptixCommand', PerformToOptixCommand())
