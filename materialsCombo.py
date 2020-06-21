from dbComboBox import dbComboBox

class materialsCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getJewelry().getMaterialCodes():
            self.addItem(a,self.getJewelry().getMaterialName(a))
        self.setCurrentCode(self.getJewelry().getProductMaterialCode(self.getCurrentRec()))
