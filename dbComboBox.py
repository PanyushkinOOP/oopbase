#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QComboBox
from rowCode import rowCode
from jewWidget import jewWidget

class dbComboBox(QComboBox,jewWidget):
    def __init__(self, jewelry=None, parent=None):
        QComboBox.__init__(self,parent)
        jewWidget.__init__(self, jewelry)
        self._jewelry = jewelry
        self.__rowCode=rowCode()
        self.setSizeAdjustPolicy(self.AdjustToContents)

    def clear(self):
        self.__rowCode.clear()
        QComboBox.clear(self)

    def addItem(self,code,text):
        self.__rowCode.appendRowCode(self.count(),code)
        QComboBox.addItem(self,text)

    def removeItem(self,index):
        self.__rowCode.removeRow(index)
        QComboBox.removeItem(self,index)

    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentIndex())

    def setCurrentCode(self,code):
        if self.__rowCode.getRow(code):
            self.setCurrentIndex(self.__rowCode.getRow(code))

    def setCurrentRec(self,value):
        self.__currentRec = value
        self.update()

    def getCurrentRec(self):
        return self.__currentRec

    def update(self):
        pass
