# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:15:04 2021

@author: Feyza
"""

#Iterable



#Iterator




sayilar=[1,2,3,4,5]      # 
iterator=iter(sayilar)   # 



while True:
    try:
        sayi=next(iterator)
        print(sayi)
    except StopIteration:
        break


# a=10
# for i in sayilar:
#     print(i)
    
# print(dir(sayilar))





# iterator=iter(sayilar)

# print(iterator)


# print(next(sayilar))
