# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0

# open a file
my_file = open('myfile.txt', 'w')

# get info of this file
print(my_file.name)
print(my_file.encoding)
print(my_file.mode)
print(my_file.closed)

my_file.write('I love code')
my_file.write('hey')
my_file.close()

# append to file
my_file = open('myfile.txt', 'a')
my_file.write('I love Java too.')
my_file.close()

# read file
my_file = open('myfile.txt', 'r+')
text = my_file.read(10)
print(text)
