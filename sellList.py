from generalList import generalList

class sellList(generalList):
  def getProduct(self,code):return self.findByCode(code).getProduct()
  def getNumber(self,code):return self.findByCode(code).getNumber()
  def getSurname(self,code):return self.findByCode(code).getSurname() 
  def getName(self,code):return self.findByCode(code).getName()
  def getSecname(self,code):return self.findByCode(code).getSecname()

  def getListSellInfo(self):
    s = ''
    for code in self.getCodes():
      s += self.findByCode(code).getSellInfo() + ',\n'
    return s[:-2]
