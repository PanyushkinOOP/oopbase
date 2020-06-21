#-*- coding:utf-8 -*-
from general import general

class material(general):
    def __init__(self, code = 0, name = "", priceforgramm = 0):
        general.__init__(self, code)
        self.setName(name)
        self.setPriceForGramm(priceforgramm)

    def setName(self, value):self.__name = value
    def setPriceForGramm(self, value):self.__priceforgramm = value
    
    def getName(self):return self.__name
    def getPriceForGramm(self):return self.__priceforgramm
    
    def getMaterialInfo(self):
        s = "Name: " + self.getName() + "\n" + "PriceForGramm: " + str(self.getPriceForGramm()) + "\n"
        return s
