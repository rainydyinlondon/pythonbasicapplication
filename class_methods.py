# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:28:57 2021

@author: Feyza
"""


class User:
    active_users=0   #Class attribute
    
    @classmethod  #decorator kullanımı
    def display_active_users(cls):
        #print(cls)
        return f"{cls.active_users} tane aktif kullanıcı var."
   
    @classmethod
    def from_string(cls,data_str):
        first,last,age=data_str.split(",")
        return cls(first,last,age)
    
    
    
    def __init__(self,first,last,age):
        print(self)
        self.first=first
        self.last=last
        self.age=age
        User.active_users+=1
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def logout(self):
        User.active_users=User.active_users-1
        return f"{self.full_name()} uygulamadan çıkış yaptı"
    
    
    

# print(User.display_active_users()) # Bir takım güncellemeler, classın ismini yazdırıyoruz.
# UserA=User("Feyza","Ç",29)
# UserB=User("Ayşe","A",30)
# UserC=User("Ayşe","A",30)

Ali=User.from_string("Ali,Korkmaz,20")

print(Ali.last)

#{"key":"value"}



# print(User.display_active_users())


# print(UserA.full_name())
# print(UserB.full_name())


# print(UserA.logout())



