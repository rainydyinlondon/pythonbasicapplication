# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:11:06 2021

@author: Feyza
"""

""" Method değil bunun adı method görünümlü property ama method gibi yazılsa da ,method gibi çağrılmıyor """

""" Eğer atama ve alma gibi işlemler için 2 ayrı metot tanımlaması yerine property tanımlamasını kullanabilirsiniz.

classmethod ise sınıf seviyesinde her bir nesneye özel olmayan metotlardır."""


class Product:
    def __init__(self,name,price,desctiption):
        self.name=name
        self.desctiption=desctiption
        if price<=0:
           raise ValueError (" Ürün fiyatı 0 dan küçük olamaz")
        else:
             self._price=price  # Private olarak tanımlanmış property oldu..
             
             
             
#Method ile değil direk değer ataması yapmak istersek... 
             
    @property  # bu şeilde yazmazsak property olmaz..       
    def price(self):
         return self._price
             
     
    @price.setter  #Nokta ile yazılıyor..
    def price(self,value):
          if value<=0:
            raise ValueError (" Değiştirelen  fiyatı 0 dan küçük olamaz")
          else:
              self._price=value 
              
    @property
    def short_description(self):
        return self.desctiption[:10]
    
              
     
     
p=Product("iphone x",9000,"Feyza Bu property Konusunu anladın mııı ???")

# print(p.price)     #Method değil farkındaysannn     

# p.price=-900
# print(p.price)

print(p.short_description)


             
#     def set_price(self,value):
#          if value<=0:
#            raise ValueError (" Değiştirelen  fiyatı 0 dan küçük olamaz")
#          else:
#               self._price=value 
    
    
#     def get_price(self):
#         return self._price
    
    
        
# p=Product("iphone x",9000)

# p.set_price(-100)
# print(p.get_price())


