# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:12:51 2021

@author: Feyza
"""

#Shuffle Methodu Kullanımı


# import random

# number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# print("Original list:", number_list)

# random.shuffle(number_list)
# print("List after first shuffle:", number_list)

# random.shuffle(number_list)
# print("List after second shuffle:", number_list)




import random


kizim_olsun =["Irmak","Asu","Nehir"]

print("Orjinal Hali Listenin :",kizim_olsun)

random.shuffle(kizim_olsun)

print("1.kez Shufflanmmış hali",kizim_olsun)

random.shuffle(kizim_olsun)
print("2.kez Shufflanmmış hali",kizim_olsun)

