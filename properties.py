# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:38:37 2021

@author: Feyza
"""
#Encapsulation


class Product:
    def __init__(self,name,price):
        self.name=name
        if price>=0:
            self._price=price
        else:
            raise ValueError(" fiyatı için negatif değer ataması yapılamaz..")
            
    @property          # DİKKATTTTTTTT
    def price(self):
        return self._price 
            
    # def set_price(self,value):
    #     if value>=0:
    #        self._price=value
    #     else:
    #         raise ValueError(" fiyatı için negatif değer ataması yapılamaz..")
            
    # """ Setters:- These are the methods used in OOPS feature which helps to set the value to private attributes in a class."""
    
    # def get_price(self,value):
    #     return self._price
    # """ #Getters:- These are the methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class."""



p=Product("iphone 12",9000)






