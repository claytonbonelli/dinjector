#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 5 de fev de 2017

@author: Clayton Bonelli
'''
from dinjector import dinjector


@dinjector.register("one")
class MyClass:
    def __init__(self):
        self.name = "clayton"


@dinjector.register(123)
class OtherClass:
    def __init__(self, pk, name):
        self.id = pk
        self.name = name
        

if __name__ == '__main__':
    o1 = dinjector.new("one")
    print(o1.name)
    
    o2 = dinjector.new(123, 1000, "john doe")
    print(o2.id)
    print(o2.name)
        