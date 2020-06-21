#-*- coding:utf-8 -*-
from jewelry import jewelry
from dataxml import dataxml as data
from datasql import datasql as new_data

jew1 = jewelry()
jew2 = jewelry()
dat1 = data()
dat2 = new_data()
dat1.read("old.xml", jew1)
dat2.write("new.sqlite", jew1)
dat2.read("new.sqlite", jew2)
