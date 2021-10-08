# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0

# a block of code which only runs when it is called.
# create function
def say_hello(name='Sam'):
    print(f'hello {name}!')


say_hello('Tony')
say_hello()


# Return values
def get_sum(num1, num2):
    total = num1 + num2
    return total


print(get_sum(1, 2))

# lambda function
get_sub = lambda num1, num2: num2 - num1

print(get_sub(2, 10))
