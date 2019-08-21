# _*_ coding: utf-8 _*_
__author__ = 'john'


list_1=["a", "b", "c", "d", "e"]
list_2=["a", "f", "c", "m"]
main_list = list(set(list_2)-set(list_1))
print(main_list)