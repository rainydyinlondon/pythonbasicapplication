# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:12:25 2021

@author: Feyza
"""

#User
#Moderator


class User:
    active_users=0  # Class seviyesinde bi properties
    @classmethod  # 
    def display_active_users(cls):
        return f"şu anda aktif {cls.active_users}"  #Class seviyesinde tanımlanan properties'i çektik .
        
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        User.active_users+=1
        
        
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
        
        

class Moderator(User):  # Inheritance alıyor...
    active_moderators=0
    @classmethod  #CLASS METHOD HIMMMMMMMMMMMM
    def display_active_moderators(cls):  #CLS  METHOD DIKKAT DIKKATTTTTTT
        return f"Şu anda aktif {cls.active_moderators} vardır..."
    
    def __init__(self,firstname,lastname,community):
         User.__init__(self,firstname,lastname)
         self.community=community # Set etmiş olduk....
         Moderator.active_moderators+=1
         
         
    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi."
    
    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir post güncelledi"
        

print(User.display_active_users())

print(Moderator.display_active_moderators())

u1=User("Ali","Dannndan")

m1=Moderator("Feyza","Ç","Yazılim")
m2=Moderator("Behzat","Ç","Polisiye")

print(m1.remove_post())
print(m2.update_post())

print(User.display_active_users())

print(Moderator.display_active_moderators())

# print(isinstance(u1,User))  # içinden türetilmiş mi ? TRUE

# print(isinstance(u1,Moderator)) # İçinden türetilmiş mi ? FALSE


# print(m1.fullname())