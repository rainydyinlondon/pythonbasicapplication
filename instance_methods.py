# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:02:56 2021

@author: Feyza
"""


class Person:
    #Yapıcı Methotlar/Constructor Method : Sınıftan içinde oluşturduğumuz olduğumuz nesnelere özel methodlardır.
    def __init__(self,name,surname,year):
        #Object attributes ,instance attributes /nesneye özel attributeslar diyebiliriz.
        self.name=name
        self.surname=surname
        self.year=year
        
    #Instance method : Object(Nesne) üzerinden oluşturduğumuz methotlara denir.
    def intro(self):  # Nesneye özel olduğu için self parametresini alıcak.
        return f"Benim adım {self.name} ve soyadım {self.surname}"
    #Instance methoddur yine aynı şekilde....   
    def calculate_age(self): #Nesneye özel olduğu için yine self parametresi alıcak....
        return f"Ve yaşım iseee {2021-self.year}"

#Object,Instance        
p1=Person("Feyza","Çerezci",1991)

print(p1.intro())  #Intro nedir ? Kaç kelimedirrr ??


print(p1.calculate_age())

