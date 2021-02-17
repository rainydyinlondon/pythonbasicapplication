# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:02:48 2021

@author: Feyza
"""


"""
Passing arguments to methods
You would like for our dogs to have a buddy. 
This should be optional, since not all dogs are as sociable.
Take a look at the setBuddy() method below. It takes self, as per usual, and buddy as arguments. 
In this case, buddy will be another Dog object. Set the self.buddy attribute to buddy, and the buddy.buddy attribute to self. 
This means that the relationship is reciprocal; you are your buddy's buddy. In this case, Filou will be Ozzy's buddy, which means that Ozzy automatically becomes Filou's buddy. 
You could also set these attributes manually, instead of defining a method, but that would require more work (writing 2 lines of code instead of 1) every time you want to set a buddy.
Notice that in Python, you don't need to specify of what type the argument is. If this were Java, it would be required.

"""



class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self
        
        
        

ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)


print(filou.buddy.name)
print(filou.buddy.age)


ozzy.buddy.doginfo()
