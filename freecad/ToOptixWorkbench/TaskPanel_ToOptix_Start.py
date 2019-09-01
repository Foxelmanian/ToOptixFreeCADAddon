#!/usr/bin/env/python
import os

from PySide.QtGui import QFileDialog, QTableWidgetItem, QHeaderView
from PySide.QtCore import Qt

import FreeCAD
import FreeCADGui

from ToOptix.OptimizationController import OptimizationController

Msg = FreeCAD.Console.PrintMessage
Log = FreeCAD.Console.PrintLog
Err = FreeCAD.Console.PrintError


class TaskPanelToOptixStart:
    """
    User interface to start ToOptix optimization process.
    """
    def getRelativeFilePath(self, relativefilename, targetfile):
        return os.path.join(os.path.dirname(relativefilename), targetfile)

    def __init__(self, analysis, msgstring, preferences_dict):
        # doc needs to be initialized first
        # self.doc = doc
        self.fea = analysis
        filename = self.getRelativeFilePath(__file__,
                                            'Qt/dlg_tooptix_start.ui')
        # this will create a Qt widget from our ui file
        self.form = FreeCADGui.PySideUic.loadUi(filename)
        self.form.textedit_fea_message.setText(msgstring)
        self.form.lineedit_ccx_binary.setText(
                preferences_dict.get("ccx_binary_path", ""))
        self.form.lineedit_working_directory.setText(
                preferences_dict.get("working_directory", ""))

        self.form.pushbutton_working_directory.clicked.connect(
                self.click_pushbutton_working_directory)
        self.form.pushbutton_ccx_binary.clicked.connect(
                self.click_pushbutton_ccx_binary)

    def click_pushbutton_working_directory(self):
        dirname = QFileDialog.getExistingDirectory(None, "", "")
        if dirname != "":
            self.form.lineedit_working_directory.setText(dirname)

    def click_pushbutton_ccx_binary(self):
        (filename, res) = QFileDialog.getOpenFileName(None, "", "")
        if filename != "":
            self.form.lineedit_ccx_binary.setText(filename)

    def accept(self):
        FreeCADGui.Control.closeDialog()

        self.fea.write_inp_file()
        working_dir = self.form.lineedit_working_directory.text()
        ccx_path = self.form.lineedit_ccx_binary.text()
        inp_path = self.fea.inp_file_name

        cpus = self.form.spinbox_cpus.value()
        files = [inp_path]
        sol_type = ["static"]
        opti_type = "seperated"
        max_iterations = self.form.spinbox_iterations.value()
        penal = 3.0
        vol_frac = 0.4
        matSets = 20
        weight_factors = [1.0]
        workDir = working_dir
        solverPath = ccx_path
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

    def reject(self):
        FreeCADGui.Control.closeDialog()

    def readTableFromList(self, mytable, mylist):
        """
        mylist contains triples of (name, value, modifyable)
        """
        mytable.clear()
        mytable.setRowCount(0)
        for (ind, (name, string_value, modifyable, var_type)) in enumerate(
                sorted(mylist, key=lambda x: x[0])):
            # sort list to get a reproducible table
            mytable.insertRow(ind)
            mytable.setItem(ind, 0, QTableWidgetItem(name))
            value_item = QTableWidgetItem(string_value)
            if not modifyable:
                value_item.setFlags(value_item.flags() & Qt.ItemIsEditable)
            mytable.setItem(ind, 1, value_item)
            type_item = QTableWidgetItem(str(var_type))
            type_item.setFlags(type_item.flags() & Qt.ItemIsEditable)

            mytable.setItem(ind, 2, type_item)

        header = mytable.horizontalHeader()

        try:
            # this is Qt4
            header.setResizeMode(0, QHeaderView.ResizeToContents)
            header.setResizeMode(1, QHeaderView.Stretch)
        except AttributeError:
            # this is Qt5
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.Stretch)

    def writeTableToList(self, mytable):
        myvars = []
        for ind in range(mytable.rowCount()):
            var_name = mytable.item(ind, 0).text()
            var_type = self.typeconverter[mytable.item(ind, 2).text()]
            var_value = mytable.item(ind, 1).text()
            var_modifyable = mytable.item(ind, 1).flags() != Qt.ItemIsEditable
            myvars.append((var_name, var_value, var_modifyable, var_type))
        return myvars
