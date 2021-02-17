# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:28:57 2021

@author: Feyza
"""


class Pet:
  
    cinsler=["kedi","kopek","kus"]
    
    def __init__(self,isim,cins):
        if cins not in  Pet.cinsler:
            raise ValueError(f"{cins} evcil bir hayvan değildir.")
        self.isim=isim
        self.cins=cins
         


    def set_cins(self,cins):
          cinsler=["kedi","kopek","kus"]
          if cins not in cinsler:
             raise ValueError(f"{cins} bir evcil hayvan değildir.")
          self.cins=cins
         
         


kopus=Pet("Paşa","kopek")
boncuk=Pet("boncuk","kedi")
mavis=Pet("mavis","kus")


mavis.set_cins("aslan")



