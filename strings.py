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

# Methods
# Capitalize
print('hello'.capitalize())

# Upper Lower
print('demo'.upper())
print('LC'.lower())

# Swap case
print('abedEFG'.swapcase())

# Get length
print(len('marvel'))

# Count
print('abide'.count('a'))

# Replace
print('John'.replace('n', 'e'))

# Starts with/End With
print("I Love You".startswith('I'))

# Split into a list
print('HelloWorld'.split('o'))

# Is all alphanumeric
print('123'.isalnum())

# Is all alphabetic
print('123a'.isalpha())

# Is all numeric
print('123b'.isnumeric())

# List
print(list('Hello W'))
