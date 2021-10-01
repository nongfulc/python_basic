# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/1
# @Version 1.0

name = 'lc'
age = 29

# Concatenate
print('My name is ' + name + ', and I am ' + str(age) + ' years old.')

# String Formatting 1: arguments by position
print('My name is {name}, and I am {age} years old'.format(name=name, age=age))

# String Formatting 2: F-Strings
print(f'My name is {name}, and I am {age} years old.')
