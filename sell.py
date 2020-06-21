#-*- coding:utf-8 -*-
from general import general

class sell(general):
    def __init__(self, code = 0, product = None, number = "", surname = "", name = "", secname = ""):
        general.__init__(self, code)
        self.setProduct(product)
        self.setNumber(number)
        self.setSurname(surname)
        self.setName(name)
        self.setSecname(secname)

    def setProduct(self, value):self.__product = value
    def setNumber(self, value):self.__number = value
    def setSurname(self, value):self.__surname = value
    def setName(self, value):self.__name = value
    def setSecname(self, value): self.__secname = value
    
    def getProductCode(self):
        if self.__product:return self.__product.getCode()
    def getProductName(self):
        if self.__product:return self.__product.getName()
        else:return ""
    def getProductTypel(self):
        if self.__product:return self.__product.getTypel()
        else:return ""
    def getProductMaterial(self):
        if self.__product:return self.__product.getMaterial()
        else:return ""
    def getProductWeight(self):
        if self.__product:return self.__product.getWeight()
        else:return ""
    def getProductPrice(self):
        if self.__product:return self.__product.getPrice()
        else:return ""
    def getProductInfo(self):
        if self.__product:return self.__product.getInfoProduct()
        else:return ""

    def getNumber(self): return self.__number
    def getSurname(self): return self.__surname
    def getName(self): return self.__name
    def getSecname(self): return self.__secname

    def getSellInfo(self):
      s=self.getProductInfo() + ' ' + ' ' + ' ' + ' '
      return s

