# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:13:17 2021

@author: Feyza
"""


#Example 1: Iterating through a string Using for Loop

# h_letters = []

# for letter in 'human':
#     h_letters.append(letter)

# print(h_letters)






# #Example 2: Iterating through a string Using List Comprehension
# # [expression for item in list] #Syntax of List Comprehension 

# h_letters = [ letter for letter in 'human' ]  # Tek bir değer olan Letter'ı döndürüyoooo.
# print( h_letters)


yenidizi=[]
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)







# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# sonuc=[(x,y) for x in adj for y in fruits]


# print(sonuc)