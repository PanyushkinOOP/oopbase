#-*- coding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys,os
from dbTableWidget import dbTableWidget

class sellsTable(dbTableWidget):
    def __init__(self, jewelry, parent = None):
        dbTableWidget.__init__(self,jewerely=jewelry,header=[u"Product",u"Number",u"Surname",u"Name",u"Secname"],parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getJewelry().getSellCodes()))
        r = 0
        for a in self.getJewelry().getSellCodes():
            self.setItem(r,0,QtWidgets.QTableWidgetItem(self.getJewelry().getSellProductName(a)))
            self.setItem(r,1,QtWidgets.QTableWidgetItem(self.getJewelry().getSellNumber(a)))
            self.setItem(r,2,QtWidgets.QTableWidgetItem(self.getJewelry().getSellSurname(a)))                                           
            self.setItem(r,3,QtWidgets.QTableWidgetItem(self.getJewelry().getSellName(a)))
            self.setItem(r,4,QtWidgets.QTableWidgetItem(self.getJewelry().getSellSecname(a)))   
            self.appendRowCode(r,a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
