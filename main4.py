#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import sys,os
sys.path.insert(0, "./jewelry")
from datasql import datasql
from dataxml import dataxml
from jewelry import jewelry
from tab import tabWidget
from PyQt5 import QtCore

app = QApplication(sys.argv)

class mainWindow(QMainWindow):
    currentChanged = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(300, 200, 800, 700)
        self.setWindowTitle(u"Jewelry Store")
        self.jewelry=jewelry()
        self.dataxml=dataxml()
        self.datasql=datasql()
        self.tabWidget=tabWidget(self.jewelry,self)
        self.tabWidget.currentChanged.connect(self.tabWidget.tabChangedSlot)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new=QAction(QIcon(),"New",self)
        self.new.setStatusTip("New database")
        self.new.triggered.connect(self.newAction)

        self.openxml=QAction(QIcon(),"Open XML",self)
        self.openxml.setStatusTip("Open data from XML")
        self.openxml.triggered.connect(self.openXMLAction)

        self.opensql=QAction(QIcon(),"Open SQL",self)
        self.opensql.setStatusTip("Open data from SQL")
        self.opensql.triggered.connect(self.openSQLAction)

        self.savexml=QAction(QIcon(),"Save XML",self)
        self.savexml.setStatusTip("Save data to XML")
        self.savexml.triggered.connect(self.saveXMLAction)

        self.savesql=QAction(QIcon(),"Save SQL",self)
        self.savesql.setStatusTip("Save data to SQL")
        self.savesql.triggered.connect(self.saveSQLAction)

        self.menubar=self.menuBar()
        self.menufile=self.menubar.addMenu("&File")
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addAction(self.opensql)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.menufile.addAction(self.savesql)
        self.statusBar()

    def newAction(self):
        self.jewelry.clear()
        self.tabWidget.update()

    def openXMLAction(self):
        filename=QFileDialog.getOpenFileName(self,u"Открыть XML",os.getcwd(),u"*.xml")[0]
        if filename:
            self.jewelry.clear()
            self.dataxml.read(filename,self.jewelry)
            self.tabWidget.update()

    def openSQLAction(self):
        filename=QFileDialog.getOpenFileName(self,u"Открыть SQL",os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.jewelry.clear()
            self.datasql.read(filename,self.jewelry)
            self.tabWidget.update()

    def saveXMLAction(self):
        filename=QFileDialog.getSaveFileName(self,u"Сохранить XML",os.getcwd(),u"*.xml")[0]
        if filename:
            self.dataxml.write(filename,self.jewelry)

    def saveSQLAction(self):
        filename=QFileDialog.getSaveFileName(self,u"Сохранить SQL",os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.datasql.write(filename,self.jewelry)

mw=mainWindow()
mw.show()
sys.exit(app.exec_())
