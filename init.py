# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:48:46 2021

@author: Feyza
"""
"""

class Product:
    def __init__(self):
        self.name="Samsung"
        self.price=2000
        print("product nesnesi oluşturuldu.")
        
    
        
p1=Product()

p2=Product()

p3=Product()

products=[p1,p2,p3]


for i in products:
    print (i.name)
    # print(type(i))

"""

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print("product nesnesi oluşturuldu.")
        
    
        
p1=Product("feyza",5000)

p2=Product("ayse",800)

p3=Product("gul",900)

products=[p1,p2,p3]


for i in products:
    print (i.name)
    # print(type(i))


