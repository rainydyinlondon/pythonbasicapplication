# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:15:50 2021

@author: Feyza
"""


class User:
    active_users=0   #Class attribute
    
    def __init__(self,name,last,age): # Constructor Method
        self.name=name
        self.last=last
        self.age=age
        User.active_users+=1  # Bir nesne oluşturulduğunda constructor methodu çalışıp , active_users değerini +1 yapıyor.
        
    def full_name(self):
        return f"{self.name} {self.last}"
    
    def logout(self):
        User.active_users=User.active_users-1
        return f"{self.full_name()} uygulamadan çıkış yaptı"


print(User.active_users)  # Program ilk çalıştığında 0 user var.  *Burada dikkat edilecek husus nesne üzerinden değil, class ile çağırım yapılıyor.
UserA=User("Feyza","Ç",29)
UserB=User("Ayşe","A",30)


print(User.active_users) # 2 adet kullanıcı oluştu...


print(UserA.full_name())  # User A 'nın ismi yazdırıldı.
print(UserB.full_name())  # User B was printed in this code.


print(UserA.logout())
# print(UserB.logout())

print(User.active_users) 