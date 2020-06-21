from dbComboBox import dbComboBox

class productsCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getJewelry().getProductCodes():
            self.addItem(a,self.getJewelry().getProductName(a))
        self.setCurrentCode(self.getJewelry().getSellProductCode(self.getCurrentRec()))
