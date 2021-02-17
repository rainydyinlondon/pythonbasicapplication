# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:48:01 2021

@author: Feyza
"""

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


import random


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
q2=Question("Feyza'nın ilk aşkı kim ?",["Burak","Ahmet","Mehmet"],"Burak")  #2.Nesnemiz
q3=Question("Feyza'nın ilk okul arkadaşı kim?",["Derya","Nazlı","Ayşe"],"Derya")  #3.Nesnemiz



sorular=[q1,q2,q3]




class Quiz:
    def __init__(self,questions):
        self.questions=questions  # içinde dizi varr o yüzden index tutmamız lazımm
        self.questionIndex=0  # ilk başta 0 vermemizin nedeni , ilk soruyu görmek istememizden kaynaklanıyorrr.
        self.score = 0
        
    def getQuestion(self):
         return self.questions[self.questionIndex]

    def displayQuestion(self):
        sorumuz=self.getQuestion()
        
        print(f"Soru{self.questionIndex +1}:{sorumuz.text}")
        for q in sorumuz.choices:
            print("-" +q)
            
        answer = input('cevap: ')
        if (sorumuz.checkAnswer(answer)):
            self.score += 1

        self.questionIndex += 1

        if len(self.questions) == self.questionIndex:
            print(self.score)
        else:
            self.displayQuestion()

Feyzaquiz=Quiz(sorular)


# print(Feyzaquiz.questions[0].text)   # Bu şekilde söylememizin sebebi questions buraya bir dizi olarak geldi...
# print(Feyzaquiz.questions[2].text)   # Bu şekilde söylememizin sebebi questions buraya bir dizi olarak geldi...


# #print(Feyzaquiz.questions[Feyzaquiz.questionIndex].text)
    
# print("------------------------------------------------------------------------------------------------")    
# print(Feyzaquiz.getQuestion().text)  # Default olarak Index 0 olduğu için bize dizinin ilk elemanını gösteriyorrr. Gelen Nesne/Obje'nin attribute'u yazdırıldıııı.
    
    
    
print(Feyzaquiz.displayQuestion())    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    