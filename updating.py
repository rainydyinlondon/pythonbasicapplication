# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:21:27 2021

@author: Feyza
"""

# with open("markalar.txt","a") as file:
#     file.write("6-BMW")



with open("markalar.txt","r+",encoding="UTF-8") as file:
    markalar=file.read()
    markalar="1-Toyota\n" +markalar
    # file.seek(0)
    # file.write("1-Toyota")
    file.seek(0)
    file.write(markalar)
with open("markalar.txt") as file:
    print(file.read())