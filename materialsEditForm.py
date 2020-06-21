#-*- coding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, QLabel
from dbListWidget import dbListWidget
from editForm import editForm
from materialsTable import materialsTable

class materialsEditForm(editForm):
    def __init__(self,jewelry=None,parent=None):
        editForm.__init__(self,tablewidget=materialsTable(jewelry=jewelry),parent=parent,jewelry=jewelry)
        
        self.__pixlabel = QLabel()

        self.__nameEdit = QLineEdit()
        self.__priceforgrammEdit = QSpinBox()
        self.__priceforgrammEdit.setRange(0, 1000000)

        self.addLabel(u"Name",0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u"PriceForGramm",1,0)
        self.addNewWidget(self.__priceforgrammEdit,1,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getJewelry().getMaterialCodes():
            self.__nameEdit.setText(self.getJewelry().getMaterialName(self.getCurrentCode()))
            self.__priceforgrammEdit.setValue(int(self.getJewelry().getMaterialPriceForGramm(self.getCurrentCode())))

    def editClick(self):
        self.getJewelry().setMaterialName(self.getCurrentCode(),self.__nameEdit.text())
        self.getJewelry().setMaterialPriceForGramm(self.getCurrentCode(),self.__priceforgrammEdit.value())
        self.tableUpdate()

    def newClick(self):
        code = self.getJewelry().getMaterialNewCode()
        self.getJewelry().newMaterial(code)
        self.getJewelry().setMaterialName(code,self.__nameEdit.text())
        self.getJewelry().setMaterialPriceForGramm(code,self.__priceforgrammEdit.value())
        self.tableUpdate()

    def delClick(self):
        self.getJewelry().removeMaterial(self.getCurrentCode())
        self.tableUpdate()
