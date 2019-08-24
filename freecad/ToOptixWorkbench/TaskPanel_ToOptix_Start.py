#!/usr/bin/env/python
import os

import FreeCADGui
from PySide.QtGui import QTableWidgetItem, QHeaderView
from PySide.QtCore import Qt


class TaskPanelToOptixStart:
    """
    User interface to start ToOptix optimization process.
    """
    def getRelativeFilePath(relativefilename, targetfile):
        return os.path.join(os.path.dirname(relativefilename), targetfile)

    def __init__(self, analysis):
        # doc needs to be initialized first
        # self.doc = doc

        filename = self.getRelativeFilePath(__file__,
                                            'Qt/dlg_tooptix_start.ui')
        # this will create a Qt widget from our ui file
        self.form = FreeCADGui.PySideUic.loadUi(filename)
        self.form.lineEdit_kind.setText("kind")
        self.form.lineEdit_name.setText("name")
        self.form.lineEdit_unique_id.setText("id")

    def accept(self):
        FreeCADGui.Control.closeDialog()

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
