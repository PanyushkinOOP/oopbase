#-*- coding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys,os
from dbTableWidget import dbTableWidget

class materialsTable(dbTableWidget):
    def __init__(self, jewelry, parent = None):
        dbTableWidget.__init__(self, jewerely=jewelry, header=[u"Name", u"PriceForGramm"], parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getJewelry().getMaterialCodes()))
        r = 0
        for a in self.getJewelry().getProductCodes():
            self.setItem(r,0,QtWidgets.QTableWidgetItem(self.getJewelry().getMaterialName(a)))
            self.setItem(r,1,QtWidgets.QTableWidgetItem(str(self.getJewelry().getMaterialPriceForGramm(a))))
            self.appendRowCode(r,a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
