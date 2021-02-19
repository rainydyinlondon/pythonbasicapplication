# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:47:11 2021

@author: Feyza
"""

liste=[1,2,3]

print(len(liste))

s="hello world"

print(len(s))



class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik=baslik
        self.yonetmen=yonetmen
        self.sure=sure
    def __str__(self):
        return f"{self.baslik},{self.yonetmen} tarafından yönetildi.."
    
    def __repr__(self):
        return f"{self.baslik},{self.yonetmen} tarafından yönetildi.."
        
    def __len__(self):
        return self.sure
   
    def __del__(self):
        print("Film objesi silindi")

f=  Film("film adı","yonetmen",120)

# print(len(f))  # TypeError: object of type 'Film' has no len()

print(str(liste))

print(str(f))

print(f)  # repper fonksiyonu nesneyi direk yazdırıyor.  
#film adı,yonetmen tarafından yönetildi.

print(len(f))  #120


del f #Film objesi silindi