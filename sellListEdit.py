from sell import sell
from sellList import sellList
from generallistedit import generalListEdit

class sellListEdit(sellList,generalListEdit):
    def newRec(self, code=0, product= None, number= '', surname= '', name= '', secname=''):
        self.appendList(sell(code, product, number, surname, name, secname))

    def setProduct(self, code, value):
        self.findByCode(code).setProduct(value)

    def setNumber(self, code, value):
        self.findByCode(code).setNumber(value)

    def setSurname(self, code, value):
        self.findByCode(code).setSurname(value)

    def setName(self, code, value):
        self.findByCode(code).setName(value)
        
    def setSecname(self, code, value):
        self.findByCode(code).setSecname(value)
        
    def getProductCode(self, code):
        return self.findByCode(code).getProductCode()

    def getProductName(self, code):
        return self.findByCode(code).getProductName()

    def getProductTypel(self, code):
        return self.findByCode(code).getProductTypel()
    
    def getProductMaterial(self, code):
        return self.findByCode(code).getProductMaterial()

    def getProductWeight(self, code):
        return self.findByCode(code).getProductWeight()

    def getProductPrice(self, code):
        return self.findByCode(code).getProductPrice()

    def getProductInfo(self, code):
        return self.findByCode(code).getProductInfo()

    def getNumber(self, code):
        return self.findByCode(code).getNumber()

    def getSurname(self, code):
        return self.findByCode(code).getSurname()
    
    def getName(self, code):
        return self.findByCode(code).getName()
    
    def getSecname(self, code):
        return self.findByCode(code).getSecname()

    def getSellInfo(self, code):
        return self.findByCode(code).getSellInfo()
    
    def getListSellInfo(self):
      s = ''
      for code in self.getCodes():
       s += self.findByCode(code).getSellInfo() + ',\n'
      return s

 
