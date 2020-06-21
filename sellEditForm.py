#-*- coding:utf-8 -*-
import os
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QPushButton,QLabel, QSizePolicy, QLineEdit
from editForm import editForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from productsCombo import productsCombo
from sellsTable import sellsTable

class sellEditForm(editForm):
    def __init__(self, jewelry, parent=None):
        editForm.__init__(self, tablewidget=sellsTable(jewelry=jewelry), parent=parent, jewelry=jewelry)

        self.__pixlabel = QLabel()

        self.__productsCombo = productsCombo(jewelry=jewelry)
        self.__numberEdit = QLineEdit()
        self.__surnameEdit = QLineEdit()
        self.__nameEdit = QLineEdit()
        self.__secnameEdit = QLineEdit()

        self.addLabel(u"Product",0,0)
        self.addNewWidget(self.__productsCombo,0,1)
        
        self.addLabel(u"Number",1,0)
        self.addNewWidget(self.__numberEdit,1,1)

        self.addLabel(u"Surname",2,0)
        self.addNewWidget(self.__surnameEdit,2,1)

        self.addLabel(u"Name",3,0)
        self.addNewWidget(self.__nameEdit,3,1)
        
        self.addLabel(u"Secname",4,0)
        self.addNewWidget(self.__secnameEdit,4,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getJewelry().getSellCodes():
            self.__productsCombo.setCurrentRec(self.getCurrentCode())
            self.__numberEdit.setText(self.getJewelry().getSellNumber(self.getCurrentCode()))
            self.__surnameEdit.setText(self.getJewelry().getSellSurname(self.getCurrentCode()))
            self.__nameEdit.setText(self.getJewelry().getSellName(self.getCurrentCode()))
            self.__secnameEdit.setText(self.getJewelry().getSellSecname(self.getCurrentCode()))
            
    def editClick(self):
        self.getJewelry().setSellProduct(self.getCurrentCode(),self.__productsCombo.getCurrentCode())
        self.getJewelry().setSellNumber(self.getCurrentCode(),self.__numberEdit.text())
        self.getJewelry().setSellSurname(self.getCurrentCode(),self.__surnameEdit.text())
        self.getJewelry().setSellName(self.getCurrentCode(),self.__nameEdit.text())
        self.getJewelry().setSellSecname(self.getCurrentCode(),self.__secnameEdit.text())
        self.tableUpdate()

    def newClick(self):
        code=self.getJewelry().getSellNewCode()
        self.getJewelry().newSell(code)
        self.getJewelry().setSellProduct(code,self.__productsCombo.getCurrentCode())
        self.getJewelry().setSellNumber(code,self.__numberEdit.text())
        self.getJewelry().setSellSurname(code,self.__surnameEdit.text())
        self.getJewelry().setSellName(code,self.__nameEdit.text())
        self.getJewelry().setSellSecname(code,self.__secnameEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getJewelry().removeSell(self.getCurrentCode())
        self.tableUpdate()
