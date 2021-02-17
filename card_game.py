# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:06:12 2021

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



class Card: 
    
    def __init__(self,tip,deger):
        self.tip=tip
        self.deger=deger
        
    # def kartıGetir(self): #Instance Method: Kart bilgilerini yazdırıcak..
    #      return f"Kart Bilgileri:{self.tip} {self.deger}"
         
    def __repr__(self):  # Repr Methodu
        return f"{self.tip} {self.deger}"

# class Deste:

#     def __init__(self):
#         kart_tipleri = ["karo","sinek","kupa","maça"]
#         kart_degerleri = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#         self.kartlar=[]
#         for tip in kart_tipleri:
#             for deger in kart_degerleri:
#                 self.kartlar.append(Card(tip,deger))
#         print(self.kartlar)
            
            
from random import shuffle  # Random kütüphanesinden + Shuffle Methodunu= Modul kullandık.     
class Deste:
      kart_tipleri = ["karo","sinek","kupa","maça"]   # Class attribute haline geldi..
      kart_degerleri = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

      def __init__(self):
      
        self.kartlar=[(tip,deger) for tip in Deste.kart_tipleri for deger in Deste.kart_degerleri]
        print(self.kartlar)
    
      def KartSayisi(self):  # Kalan kart sayısını bulmak için
           return len(self.kartlar) 
      
      def KartlariKaristir(self): #Random, shuffle, random.sample
          if (self.KartSayisi()<52):
              raise ValueError("Deste Bozulmadan kartları karıştırabilirsiniz..")
      
          shuffle(self.kartlar)
      
      def kartDagit(self,adet):  #Belirtilen adet kadar kart dağıtılmalıdır.  Destedeki kalan kart sayısına dikkat.
          kartSayisi=self.KartSayisi()
          if kartSayisi == 0:
              raise ValueError("Bütün kartlar dağıtıldı.")
          adet=min([kartSayisi,adet])
          kartlar= self.kartlar[-adet:] #Sondan seçiyoruz kartları
          self.kartlar=self.kartlar[:-adet]
          return kartlar
      
      def kartAt(self): #ismindeki metot elden bir kart atmak için kullanılsın.
          return self.kartDagit(1)[0]
     


deste1=Deste()



deste1.KartlariKaristir()
print(deste1.kartlar)
deste1.kartDagit(50)
print(deste1.KartSayisi())  # 52-10 =42 kart kaldıı
print(deste1.kartlar)
print(deste1.kartAt())

print(deste1.kartlar)

sinek5 = Card("sinek","5")
karoAs = Card("karo","A")























