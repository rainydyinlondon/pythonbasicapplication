# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:53:02 2021

@author: Feyza
"""

class Product:
    def __init__(self,name,price):    #Oluşturulan Nesne için çalışacak kodlar
        self.name=name
        if price>=0:  # (self,name,price): parametre olarak gelicek değer >=0 mı diye kontrol ediyoruz...
            self._price=price  #Encapsulation kafası..
        else:
            raise ValueError(" Heyyy seni çılgın  fiyatı için negatif değer ataması yapılamaz...")
     
    #Decorator Kullanımı
    @property
    def price(self):  #Get komutu gibi düşünebilirsin..
        return self._price
    
    @price.setter  # Bilgi set etme olanağını sağlıyor  / def set_price(self,value):  gibi düşünebilirsin....
    def price(self,value):
        if value>=0:  # (self,value): dışardan gönderilen/ (parametre olarak gelicek değer)  >=0 mı diye kontrol ediyoruz...
            self._price=value  
        else:
            raise ValueError("Rainyy Ürün fiyatı için negatif değer ataması yapılamaz...")
     
    
            
            

p=Product("Iphone",9000)

# print(p.price)

p.price=-8000 
print(p.price)  #    @price.setter   çalıştırıldı...
    
            
    # def set_price(self,value):
    #     if value>=0:  # (self,value): parametre olarak gelicek değer >=0 mı diye kontrol ediyoruz...
    #        self._price=value  
    #     else:
    #         raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz...")
     
    
    # def get_price(self):
    #     return self._price
    
        

# p=Product("Iphone",9000)

# p.set_price(900)
# # p.price=-900
# """print(p.price)  # Bu şekilde çağıramıyoruz çünkü ..... AttributeError: 'Product' object has no attribute 'price' """


# p.get_price()