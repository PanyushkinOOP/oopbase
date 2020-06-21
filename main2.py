from jewelry import jewelry
from dataxml import dataxml as data

jew1=jewelry()
dat1=data()
dat1.read('old.xml',jew1)
jew1.newMaterial(code=5, name='Steal',priceforgramm=200)
jew1.newProduct(code=6,name='Starlight',typel='Ring',material=jew1.findMaterialByCode(4),weight=30,price=6000)
jew1.newSell(code=6,product=jew1.findProductByCode(6),number='+7906',surname='Babulev',name='Nikolay',secname='Alexandrovich')
jew1.removeMaterial(5)
jew1.removeProduct(6)
jew1.removeSell(2)
dat1.write('new.xml',jew1)
