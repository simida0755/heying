# _*_ coding: utf-8 _*_
__author__ = 'john'


class Test:

    def __init__(self):
        self.a = 'a'

    @property
    def b(self):
        return 'b'
test = Test()
print(test.__dict__)