#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QTabWidget
import sys,os
from materialsEditForm import materialsEditForm
from productEditForm import productEditForm
from sellEditForm import sellEditForm
from PyQt5.QtCore import pyqtSlot

class tabWidget(QTabWidget):
    def __init__(self, jewelry, parent=None):
        QTabWidget.__init__(self,parent)
        self.__sellEditForm=sellEditForm(jewelry=jewelry)
        self.addTab(self.__sellEditForm,u"Sell")
        self.__productEditForm=productEditForm(jewelry=jewelry)
        self.addTab(self.__productEditForm,u"Product")
        self.__materialsEditForm=materialsEditForm(jewelry=jewelry)
        self.addTab(self.__materialsEditForm,u"Material")

    def update(self):
        self.__materialsEditForm.tableUpdate()
        self.__productEditForm.tableUpdate()
        self.__sellEditForm.tableUpdate()

    @pyqtSlot(int)
    def tabChangedSlot(self,argTabIndex):
        self.__sellEditForm.tableUpdate()
