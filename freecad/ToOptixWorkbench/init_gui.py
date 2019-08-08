#!/usr/bin/env/python

# import platform
# import os
# import sys

import FreeCAD
import FreeCADGui

Msg = FreeCAD.Console.PrintMessage
Log = FreeCAD.Console.PrintLog
Err = FreeCAD.Console.PrintError

# access to the resource file
# from freecad.ToOptixWorkbench import resources_rc


class ToOptixWorkbench(FreeCADGui.Workbench):
    """
    A FreeCAD workbench for topology optimization.
    """

    Icon = ":/icons/blub.svg"

    MenuText = "Topology Optimization (ToOptix)"
    ToolTip = "Topology Optimization with Python and Calculix"

    def GetClassName(self):
        return "Gui::ToOptixWorkbench"

    def Initialize(self):
        self.appendToolbar("ToOptix",
                           [
                            "PerformToOptixCommand"
                           ])
        self.appendMenu("ToOptix",
                        [
                         "PerformToOptixCommand"
                        ])

    def ContextMenu(self, recipient):
        selection = [s for s in FreeCADGui.Selection.getSelection()
                     if s.Document == FreeCAD.ActiveDocument]
        Log("selection: " + str(selection) + "\n")
        Log("recipient: " + str(recipient) + "\n")

    def Activated(self):
        pass

    def Deactivated(self):
        pass


FreeCADGui.addWorkbench(ToOptixWorkbench())
