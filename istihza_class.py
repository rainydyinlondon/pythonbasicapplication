# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:18:29 2021

@author: Feyza
"""


# sesli_harfler = 'aeıioöuü'
# sayaç = 0

# kelime = input('Bir kelime girin: ')

# for harf in kelime:
#     if harf in sesli_harfler:
#         sayaç += 1

# # mesaj = '{} kelimesinde {} sesli harf var.'
# # print(mesaj.format(kelime, sayaç))


# mesaj = f"{kelime} kelimesinde {sayaç} sesli harf var."

# print(mesaj)



sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

for harf in kelime:  
    if seslidir(harf):  #Burda method çağırılıyor, kodlar satır satır derlendiği için öncesinde def(sesli) methodu tanımlanmalı..
        sayaç += 1


mesaj = f"{kelime} kelimesinde {sayaç} sesli harf var."

print(mesaj)
