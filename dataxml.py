#-*- coding:utf-8 -*-
import os
import xml.dom.minidom

class dataxml:
    def read(self, inp, jew):
        dom = xml.dom.minidom.parse(inp)
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "material"):
                code, name, priceforgramm = 0, "", 0
                for t in node.attributes.items():
                    if t[0] == "code":code = int(t[1])
                    if t[0] == "name":name = t[1]
                    if t[0] == "priceforgramm":priceforgramm = int(t[1])
                jew.newMaterial(code, name, priceforgramm)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "product"):
                code, name, typel, material, weight, price = 0, "", "", None, 0, 0
                for t in node.attributes.items():
                    if t[0] == "code":code = int(t[1])
                    if t[0] == "name":name = t[1]
                    if t[0] == "typel":typel = t[1]
                    if t[0] == "material":material = jew.findMaterialByCode(int(t[1]))
                    if t[0] == "weight":weight = float(t[1])
                    if t[0] == "price":price = int(t[1])
                jew.newProduct(code, name, typel, material, weight, price)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "sell"):
                code, product, number, surname, name, secname = 0, None, "", "", "", ""
                for t in node.attributes.items():
                    if t[0] == "code":code = int(t[1])
                    if t[0] == "product":product = jew.findProductByCode(int(t[1]))
                    if t[0] == "number":number = t[1]
                    if t[0] == "surname":surname = t[1]
                    if t[0] == "name":name = t[1]
                    if t[0] == "secname":secname = t[1]
                jew.newSell(code, product, number, surname, name, secname)

    def write(self, out, jew):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("jewelry")
        dom.appendChild(root)
        for c in jew.getProductCodes():
            mat = dom.createElement("material")
            mat.setAttribute("code", str(c))
            mat.setAttribute("name", jew.getMaterialName(c))
            mat.setAttribute("priceforgramm", str(jew.getMaterialPriceForGramm(c)))
            root.appendChild(mat)
        for c in jew.getProductCodes():
            cust = dom.createElement("product")
            prod.setAttribute("code", str(c))
            prod.setAttribute("name", jew.getProductName(c))
            prod.setAttribute("typel", jew.getProductTypel(c))
            prod.setAttribute("material", str(jew.getProductMaterialCode(c)))
            prod.setAttribute("weight", str(jew.getProductPrice(c)))
            prod.setAttribute("price", str(jew.getProductPrice(c)))
            root.appendChild(prod)
        for c in jew.getSaleCodes():
            sel = dom.createElement("sell")
            sel.setAttribute("code", str(c))
            sel.setAttribute("product", str(jew.getSellProductCode(c)))
            sel.setAttribute("number", jew.getSellNumber(c))
            sel.setAttribute("surname", jew.getSellSurname(c))
            sel.setAttribute("name", jew.getSellName(c))
            sel.setAttribute("secname", jew.getSellSecname(c))
            root.appendChild(sel)
        f = open(out, "w")
        f.write(dom.toprettyxml())
