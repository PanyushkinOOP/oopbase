#-*- coding:utf-8 -*-
import os
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QPushButton,QLabel, QSizePolicy, QLineEdit, QDoubleSpinBox, QSpinBox
from editForm import editForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from materialsCombo import materialsCombo
from productsTable import productsTable

class productEditForm(editForm):
    def __init__(self, jewelry, parent=None):
        editForm.__init__(self, tablewidget=productsTable(jewelry=jewelry), parent=parent, jewelry=jewelry)

        self.__pixlabel = QLabel()

        self.__nameEdit = QLineEdit()
        self.__typelEdit = QLineEdit()
        self.__materialsCombo = materialsCombo(jewelry=jewelry)
        self.__weightEdit = QDoubleSpinBox()
        self.__priceEdit = QSpinBox()
        self.__priceEdit.setRange(0, 1000000)

        self.addLabel(u"Name",0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        
        self.addLabel(u"Typel",1,0)
        self.addNewWidget(self.__typelEdit,1,1)

        self.addLabel(u"Material",2,0)
        self.addNewWidget(self.__materialsCombo,2,1)

        self.addLabel(u"Weight",3,0)
        self.addNewWidget(self.__weightEdit,3,1)
        
        self.addLabel(u"Price",4,0)
        self.addNewWidget(self.__priceEdit,4,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getJewelry().getProductCodes():
            self.__nameEdit.setText(self.getJewelry().getProductName(self.getCurrentCode()))
            self.__typelEdit.setText(self.getJewelry().getProductTypel(self.getCurrentCode()))
            self.__materialsCombo.setCurrentRec(self.getCurrentCode())
            self.__weightEdit.setValue(int(self.getJewelry().getProductWeight(self.getCurrentCode())))
            self.__priceEdit.setValue(int(self.getJewelry().getProductPrice(self.getCurrentCode())))
            
    def editClick(self):
        self.getJewelry().setProductName(self.getCurrentCode(),self.__nameEdit.text())
        self.getJewelry().setProductTypel(self.getCurrentCode(),self.__typelEdit.text())
        self.getJewelry().setProductMaterial(self.getCurrentCode(),self.__materialsCombo.getCurrentCode())
        self.getJewelry().setProductWeight(self.getCurrentCode(),self.__weightEdit.value())
        self.getJewelry().setProductPrice(self.getCurrentCode(),self.__priceEdit.value())
        self.tableUpdate()

    def newClick(self):
        code=self.getJewelry().getProductNewCode()
        self.getJewelry().newProduct(code)
        self.getJewelry().setProductName(code,self.__nameEdit.text())
        self.getJewelry().setProductTypel(code,self.__typelEdit.text())
        self.getJewelry().setProductMaterial(code,self.__materialsCombo.getCurrentCode())
        self.getJewelry().setProductWeight(code,self.__weightEdit.value())
        self.getJewelry().setProductPrice(code,self.__priceEdit.value())
        self.tableUpdate()

    def delClick(self):
        self.getJewelry().removeProduct(self.getCurrentCode())
        self.tableUpdate()
