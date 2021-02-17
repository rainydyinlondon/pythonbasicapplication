# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:00:50 2021

@author: Feyza
"""


# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.




class Comment:
    def __init__(self,username,text,likes,dislikes):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislikes
    

    
c1=Comment("feyza","burak","likes","dislikes")
c2=Comment("d","ff","likes","dislikes")
c3=Comment("dsd","bufeerak","likes","dislikes")
c4=Comment("sdsd","bureeak","likes","dislikes")
c5=Comment("adasds","eeburak","likes","dislikes")

comments=[c1,c2,c3,c4,c5]


for i in comments:
    print(i.username,i.text,i.likes,i.dislikes)
    
    
    
#fstring kullanımını ööğrennn