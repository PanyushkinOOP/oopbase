#-*- coding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys,os
from dbTableWidget import dbTableWidget

class productsTable(dbTableWidget):
    def __init__(self, jewelry, parent = None):
        dbTableWidget.__init__(self,jewerely=jewelry,header=[u"Name",u"Typel",u"Material",u"Weight",u"Price"],parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getJewelry().getProductCodes()))
        r = 0
        for a in self.getJewelry().getProductCodes():
            self.setItem(r,0,QtWidgets.QTableWidgetItem(self.getJewelry().getProductName(a)))
            self.setItem(r,1,QtWidgets.QTableWidgetItem(self.getJewelry().getProductTypel(a)))
            self.setItem(r,2,QtWidgets.QTableWidgetItem(self.getJewelry().getProductMaterialName(a)))                                            
            self.setItem(r,3,QtWidgets.QTableWidgetItem(str(self.getJewelry().getProductWeight(a))))
            self.setItem(r,4,QtWidgets.QTableWidgetItem(str(self.getJewelry().getProductPrice(a))))
            self.appendRowCode(r,a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
