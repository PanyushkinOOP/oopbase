from materialList import materialList
from generallistedit import generalListEdit
from material import material

class materialListEdit(materialList,generalListEdit):
    def newRec(self, code = 0, name = "", priceforgramm = 0):
        self.appendList(material(code, name, priceforgramm))
        
    def setName(self, code, value):
        self.findByCode(code).setName(value)

    def setPriceForGramm(self, code, value):
        self.findByCode(code).setPriceForGramm(value)
    
    def getName(self, code):
        return self.findByCode(code).getName()

    def getPriceForGramm(self,code):
        return self.findByCode(code).getPriceForGramm()
        
    def getMaterialInfo(self, code):
        return self.FindByCode(code).getMaterialInfo()

