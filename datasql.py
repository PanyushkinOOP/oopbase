#-*- coding:utf-8 -*-
import os
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;
create table material
(code integer primary key,
    name text,
    priceforgramm integer);
create table product
(code integer primary key,
    name text,
    typel text,
    material integer,
    weight float,
    price integer);
create table sell
(code integer primary key,
    product integer,
    number text,
    surname text,
    name text,
    secname text); 
"""

class datasql:
    def read(self, inp, jew):
        conn = db.connect(inp)
        curs = conn.cursor()

        curs.execute("select code, name, priceforgramm from material")
        data = curs.fetchall()
        for r in data:jew.newMaterial(r[0], r[1], r[2])

        curs.execute("select code, name, typel, material, weight, price from product")
        data = curs.fetchall()
        for r in data:jew.newProduct(r[0], r[1], r[2], jew.findMaterialByCode(r[3]), r[4], r[5])

        curs.execute("select code, product, number, surname, name, secname from sell")
        data = curs.fetchall()
        for r in data:jew.newSell(r[0], jew.findProductByCode(r[1]), r[2], r[3], r[4], r[5])

    def write(self, out, jew):
        if os.path.isfile(out):
            os.remove(out)
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(emptydb)

        for c in jew.getMaterialCodes():
            curs.execute("insert into material(code, name, priceforgramm) values('%s', '%s', '%s')" % (str(c),
                jew.getMaterialName(c),
                str(jew.getMaterialPriceForGramm(c))))
        for c in jew.getProductCodes():
            curs.execute("insert into product(code, name, typel, material, weight, price) values('%s', '%s', '%s', '%s', '%s', '%s')" % (str(c),
                jew.getProductName(c),
                jew.getProductTypel(c),
                str(jew.getProductMaterialCode(c)),
                str(jew.getProductWeight(c)),
                str(jew.getProductPrice(c))))
        for c in jew.getSellCodes():
            curs.execute("insert into sell(code, product, number, surname, name, secname) values('%s','%s','%s', '%s','%s','%s')" % (str(c),
                str(jew.getSellProductCode(c)),
                jew.getSellNumber(c),
                jew.getSellSurname(c),
                jew.getSellName(c),
                jew.getSellSecname(c)))
    
        conn.commit()
        conn.close()
