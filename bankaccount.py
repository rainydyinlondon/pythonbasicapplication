# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:14:48 2021
# BankAccount isminde bir sınıf tanımlayınız.
# Üretilen her bir nesne owner isminde biz özelliğe sahip olmalıdır. BankAccount("Sadık Turan")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
# Üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance
# üzerine ekleyin ve balance miktarını geriye döndürün.
# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
# değerinden çıkarıp geriye döndürün.

# hesap = BankAccount("Feyza")
# hesap.owner => 
# hesap.balance => 0.0
# hesap.deposit(1000) => 1000.0
# hesap.withdraw(500) => 500.0

@author: Feyza
"""


class BankAccount:
    #Yapıcı methotlat :Nesneye attribute kazandırıyor
    def  __init__(self,owner):  #constructor method
        self.owner=owner
        self.balance=0.0
       #Nesneye hizmet edecek metotlar da işte Instance Method         
    def getBalance(self): #ınstance method veya Instance attribute
        return self.balance
        
    def deposit(self,miktar):   # Instance Method
        self.balance=self.balance+miktar
        return self.balance
        
    def withdraw(self,miktar): #Instance Method
       self.balance=self.balance-miktar
       return self.balance
    
        
        
b1=BankAccount("Feyza")

print(b1.getBalance())
        
print(b1.owner)
    
print(b1.balance)    

print(b1.deposit(1000))

print(b1.deposit(1000))


print(b1.getBalance())

print(b1.withdraw(500))

    
    

