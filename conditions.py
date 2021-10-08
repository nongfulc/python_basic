# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0

# if/else
x = 1
y = 2
if x > y:
    print('yyds')
else:
    print('bullshit')

# elif
if x > y:
    print('a')
elif x == y:
    print('b')
else:
    print('c')

# nested if
if x > 1 and x < y:
    print('hello')

if x == y or y < 10:
    print('hehe')

if not (x == y):
    print('cccc')

# in /not in
nums = [1, 2, 3, 4]
if 9 in nums:
    print(9)
if 1 not in nums:
    print(1)

# is / is not
if x is y:
    print(x is y)
if x is not y:
    print(x is y)
