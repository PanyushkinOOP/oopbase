#-*- coding:utf-8 -*-
from productListEdit import productListEdit
from sellListEdit import sellListEdit
from materialListEdit import materialListEdit

class jewelry():
    def __init__(self):
        self.__product = productListEdit()
        self.__material = materialListEdit()
        self.__sell = sellListEdit()
    
    def removeMaterial(self, code):
        a = True
        for c in self.__product.getCodes():
            if code == self.__product.getMaterialCode(c):
                a = False
                break
        if a:
            self.__material.removeList(code)

    def removeProduct(self, code):
        a = True
        for c in self.__sell.getCodes():
            if code == self.__sell.getProductCode(c):
                a = False
                break
        if a:
            self.__product.removeList(code)

    def clear(self):
        self.__sell.clear()
        self.__product.clear()
        self.__material.clear()
    def newMaterial(self, code = 0, name = "", priceforgramm = 0):
        self.__material.newRec(code, name, priceforgramm)
    def findMaterialByCode(self,code):return self.__material.findByCode(code)
    def getMaterialNewCode(self):return self.__material.getNewCode()
    def getMaterialCodes(self):return self.__material.getCodes()
    def getMaterialName(self,code):return self.__material.getName(code)
    def getMaterialPriceForGramm(self,code):return self.__material.getPriceForGramm(code)
    def getMaterialNewCode(self):return self.__material.getNewCode()

    def setMaterialName(self, code, value):self.__material.setName(code,value)
    def setMaterialPriceForGramm(self,code,value):self.__material.setPriceForGramm(code,value)

    def newProduct(self,code=0,name = "", typel = "", material = None, weight = 0, price = 0):
        self.__product.newRec(code, name, typel, material, weight, price)
    def findProductByCode(self,code):return self.__product.findByCode(code)
    def getProductCodes(self):return self.__product.getCodes()
    def getProductName(self, code):return self.__product.getName(code)
    def getProductTypel(self, code):return self.__product.getTypel(code)

    def getProductMaterialCode(self,code):return self.__product.getMaterialCode(code)
    def getProductMaterialName(self,code):return self.__product.getMaterialName(code)
    def getProductMaterialPriceForGramm(self,code):return self.__product.getMaterialPriceForGramm(code)

    def getProductWeight(self,code):return self.__product.getWeight(code)
    def getProductPrice(self, code):return self.__product.getPrice(code)
    def getProductNewCode(self):return self.__product.getNewCode()

    def setProductName(self, code, value):self.__product.setName(code, value)
    def setProductTypel(self, code, value):self.__product.setTypel(code, value)
    def setProductMaterial(self, code, pcode):self.__product.setMaterial(code, self.findMaterialByCode(pcode))
    def setProductWeight(self, code, value):self.__product.setWeight(code, value)
    def setProductPrice(self, code, value):self.__product.setPrice(code, value)

    def removeSell(self, code):self.__sell.removeList(code)
    def newSell(self, code=0, product = None, number = "", surname = "", name = "", secname = ""):self.__sell.newRec(code, product, number, surname, name, secname)
    def findSellByCode(self, code):return self.__sell.findByCode(code)

    def setSellProduct(self, code, pcode):self.__sell.setProduct(code, self.findProductByCode(pcode))
    def setSellNumber(self, code, value):self.__sell.setNumber(code, value)
    def setSellSurname(self, code, value):self.__sell.setSurname(code, value)
    def setSellName(self, code, value):self.__sell.setName(code, value)
    def setSellSecname(self, code, value):self.__sell.setSecname(code, value)

    def getSellCodes(self):return self.__sell.getCodes()
    def getSellNewCode(self):return self.__sell.getNewCode()
    def getSellProductCode(self,code):return self.__sell.getProductCode(code)
    def getSellProductName(self,code):return self.__sell.getProductName(code)
    def getSellProductTypel(self, code):return self.__sell.getProductTypel(code)
    def getSellProductMaterial(self, code):return self.__sell.getProductMaterial(code)
    def getSellProductWeight(self, code):return self.__sell.getProductWeight(code)
    def getSellProductPrice(self, code):return self.__sell.getProductPrice(code)
    def getSellNumber(self, code):return self.__sell.getNumber(code)
    def getSellSurname(self, code):return self.__sell.getSurname(code)
    def getSellName(self, code):return self.__sell.getName(code)
    def getSellSecname(self, code):return self.__sell.getSecname(code)
