# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:00:27 2021

@author: Feyza
"""

#Encapsulation (Nesne dışından erişilmeyen şeye _ private olarak tanımlama işlemi pythonda...)

class Product:
     def __init__(self,name,price,description):
         self.name=name
         self.description=description
         if price>=0:
             self._price=price  #_ (encapsulation)
         
         else:
             self._price=0
             
     @property        
     def price(self):  # - olmayan versiyonunu kullandıkkk, dışarıya açmak istediğimizideee..
         return self._price
      
     @price.setter
     def price(self,value):
          if value>=0:
              self._price=value  #_ encapsulationn
         
          else:
              raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz...") 
     @property
     def short_description(self):
         return self.description[:6]
    

     # def set_price(self,value):  # Setle set ediyoruz
     #     if value>=0:
     #         self._price=value  #_ encapsulationn
         
     #     else:
     #         raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz...")
    
    
    
     # def get_price(self): # Get ile alıyoruzz...
     #    return self._price
             
    
        
p=Product("iphone12 ",-9000,"Iphone Ürün fiyatı için negatif değer ataması yapılamaz")
# print(p.price)
print(p.short_description)


# print(p.get_price())

# p.set_price(100)

# print(p.get_price())

# p.set_price(-8100)

# print(p.get_price())