# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:30:11 2021

@author: Feyza
"""




# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

# q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
# q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
# q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

# sorular = [q1,q2,q3]

# # Quiz sınıfı
# #   Instance Attributes
# #       - questions, questionIndex, score
# #   Instance Methods
# #       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
# #       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
# #       - loadQuestion()        => Testi başlatır.
# #       - displayScore()        => Score bilgisini gösterir.
# #       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)




class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
        
        
    def checkAnswer(self,answer): # Instance Method
         if answer not in self.choices:   # Normalde Bu else komutunu yazmasan Sadece bize false değer döndürüyor ama Biz Daha insani bir şey istiyoruzz. O yüzdenn Yaneee
             raise  ValueError("Hatalı bilgi")  # Meali de şöyle : Ürettiğin nesnenin içindeki choiceslardan bir tanesi değilse , dışarıdan verilen answer o zaman "Hatalı Bilgi" yazdırıyorrr.
         return self.answer== answer # Geriye True değeri döndürülüyorrr...
      
        



q1=Question("Feyza şirketinin ismini ne koymalı ?",["FeyzaLdt","FeyzaSeymaLtd","RainyDayInLondon"],"RainyDayInLondon")  # NESNE OLUŞTURDUKK.


# print(q1.answer)
# print(q1.text)
# print(q1.choices)    
    
    
print(q1.checkAnswer("python"))  # False değer döndürmesinin sebebi saçma bir şey DIŞARDAN demiş  olmannnn(Python Ne manaaaaaaaaaaaa)  # ARTIK FASE GELMİYOR ValueErrordan dolayıı
print(q1.checkAnswer("RainyDayInLondon")) # True değer döndürüyor çünkü,  DIŞARIDAN GELEN  cevap ile , ürettiğimiz nesnenin cevabu aynııııııı







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    