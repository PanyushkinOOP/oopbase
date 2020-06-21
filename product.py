#-*- coding:utf-8 -*-
from general import general

class product(general):
    def __init__(self, code = 0, name = "", typel = "", material = None, weight = 0, price = 0):
        general.__init__(self, code)
        self.setName(name)
        self.setTypel(typel)
        self.setMaterial(material)
        self.setWeight(weight)
        self.setPrice(price)

    def setName(self, value):self.__name = value
    def setTypel(self, value):self.__typel = value
    def setMaterial(self, value):self.__material = value
    def setWeight(self, value):self.__weight = value
    def setPrice(self, value): self.__price = value

    def getName(self): return self.__name
    def getTypel(self): return self.__typel

    def getMaterialCode(self):
        if self.__material:return self.__material.getCode()
    def getMaterialName(self):
        if self.__material:return self.__material.getName()
        else:return ""
    def getMaterialPriceForGramm(self):
        if self.__material:return self.__material.getPriceForGramm()
        else:return ""
    def getMaterialInfo(self):
        if self.__material:return self.__material.getInfoMaterial()
        else:return ""
    
    def getWeight(self): return self.__weight
    def getPrice(self): return self.__price

    def getProductInfo(self):
      s=' ' + ' ' + self.getMaterialInfo() + str(self.getWeight()) + str(self.getPrice())
      return s
