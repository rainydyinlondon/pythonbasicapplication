# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:48:29 2021

@author: Feyza
"""
#Inheritance
#Method ezme : Overriding


class Person:
       def __init__(self,name,surname,age):
           self.name=name
           self.surname=surname
           self.age=age
           print("Person Nesnesi Türetildi...") 
         
         
       def intro(self):
            print(self.name,self.surname,self.age)
            
class Student(Person):  #Person'dan kalıtım aldı...
      def __init__(self,name,surname,age,number):
         Person.__init__(self,name,surname,age)   # BASE SINIFIN PARAMETRELERİ ÇALIŞMASI İÇİN......
         print("Student Nesneni türetildi....")
         self.number=number
         
      def study(self):
          print(f"{self.number} numaralı öğrenci ders çalışıyor.. ")

      def intro(self):
           print(self.name,self.surname,self.age,self.number)   # Aynı isimli method kullanmamıza rağmen ,ilgili methodu ezmiş oluyoruz..
            
class Teacher(Person):
     def __init__(self,name,surname,age,branch):  # İlave edilecek yeni özellik sonuna ekleniyorrrr.
         super().__init__(name,surname,age)   # Sınıf ismi ve self kullanmak istemezsek bu şekilde de yapabiliriz...
         self.branch=branch
         
     def teach(self):
         print(f"{self.name} isimli öğretmen {self.branch} dersini veriyor...")
                 




p1=Person("Feyza","Ç",29)
print("----------------------------------")

p1.intro()  #PERSON içerisindeki

print("----------------------------------")

s1=Student("Ayşe","A",29,5)
s1.intro()

print("----------------------------------")

s1.study()


print("----------------------------------")

t1=Teacher("Ayşe","A",29,"İngilizce")
t1.teach()

print("----------------------------------")

t1.intro()
print(t1.branch)

print("----------------------------------")
