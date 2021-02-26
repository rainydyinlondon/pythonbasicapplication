# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:31:27 2021

@author: Feyza
"""

# "w" (write) yazma modumuz
# ** Dosyayı konumda oluşturu
# ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.



with open("newfile.txt","w",encoding="UTF-8") as file:  
    #farklı bir klasörde oluşturmak istersekkk eğer "C:/users/KeepCoding vs. vs şeklinde sekmeler oluşturulur...

# file =open("newfile.txt","w",encoding="UTF-8")  
    file.write("Feyza  Burak\n")
    file.write("Burak  Burak\n")
    file.write("Feyza  Feyza\n")
    file.close()
    print(file)
    
    
with open("newfile.txt")as file:
     print(file.read())