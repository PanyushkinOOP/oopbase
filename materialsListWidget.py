#-*- coding:utf-8 -*-
from dbListWidget import dbListWidget

class materialsListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getJewelry().getProductMaterialCodes(self.getCurrentRec()):
        if self.getJewelry().getProductMaterialCodes(self.getCurrentRec()):
            self.setCurrentRow(0)
