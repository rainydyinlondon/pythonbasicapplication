# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:57:44 2021

@author: Feyza
"""

class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a