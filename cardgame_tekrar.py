# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:35:03 2021

@author: Feyza
"""


# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek.
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)

# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.

# sinek5.kartıGetir() => sinek 5

# Deste sınıfı

# deste1 = Deste()

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.
# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.



# class Quiz:
#     def __init__(self,questions):  # Soruları burda set etmiş olduk
#         self.questions = random.sample(questions, len(questions))
#         self.questionIndex = 0
#         self.score = 0
from random import shuffle 
class Kart: 
    
    def __init__(self,tip,deger):
        self.tip=tip
        self.deger=deger
        
    def kartıGetir(self): #Instance Method: Kart bilgilerini yazdırıcak..
          return f"Kart Bilgileri:{self.tip} {self.deger}"
         
    def __repr__(self):  # Repr Methodu
        return f"{self.tip} {self.deger}"
    
    
class Deste:
      tipler=["karo","sinek","kupa","maça"]
      degerler=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
      def __init__(self):
          self.kartlar=[Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]  #Kart nesnesine gönderiyoruz Kart(tip,deger)
          print(self.kartlar)
        
      def KartSayisi(self):
          return len(self.kartlar)
      
      def KartlariKaristir(self):
          if (self.KartSayisi()<52):
              raise ValueError("Deste Bozulmadan kartları karıştırabilirsiniz..")
          shuffle(self.kartlar)
     
          
      def KartDagit(self,adet):
          kartSayisi=self.KartSayisi() #Fonksiyon çağırılıcak
          if kartSayisi==0:
              raise ValueError("Bütün Kartlar Dağıtıldı...")
          adet=min([kartSayisi,adet])
          kartlar= self.kartlar[-adet:]
          self.kartlar=self.kartlar[:adet]
          return kartlar



deste1=Deste()

deste1.KartlariKaristir()
print("--------------------------------------------------------------------------------")


print(deste1.KartSayisi())



print("--------------------------------------------------------------------------------")



print(deste1.KartDagit(2))
    
print("--------------------------------------------------------------------------------")




print(deste1.KartSayisi())
    
    
    
    
    
    
    
    
    
    