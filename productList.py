from generalList import generalList

class productList(generalList):
  def getName(self,code):return self.findByCode(code).getName()
  def getTypel(self,code):return self.findByCode(code).getTypel()
  def getMaterial(self,code):return self.findByCode(code).getMaterial() 
  def getWeight(self,code):return self.findByCode(code).getWeight()
  def getPrice(self,code):return self.findByCode(code).getPrice()

  def getListProductInfo(self):
    s = ''
    for code in self.getCodes():
      s += self.findByCode(code).getProductInfo() + ',\n'
    return s[:-2]
