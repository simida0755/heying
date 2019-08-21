# _*_ coding: utf-8 _*_
__author__ = 'john'

class book:
    def __init__(self,dict):
        self.a = dict['a']
        self.b = dict['b']

    @property
    def c(self):
        return