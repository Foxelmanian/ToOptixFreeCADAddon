#!/usr/bin/env/python

import FreeCAD
import FreeCADGui
from PySide import QtGui


class PerformToOptixCommand:
    "Performs ToOptix topology optimization"

    def GetResources(self):
        return {"MenuText": "Topology Optimization",
                "Accel": "",
                "ToolTip": "Performs topology optimization",
                "Pixmap": ":/icons/bla.svg"
                }

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True

    def Activated(self):

        pass

print("command to be added")
FreeCADGui.addCommand('PerformToOptixCommand', PerformToOptixCommand())
