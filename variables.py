# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/1
# @Version 1.0

"""
变量名命名规则：
1. 大小写敏感；
2. 下划线或者字母开头；
3. 不能以数字开头；
4. 不需要声明变量；
"""

# int
x = 1
# float
y = 2.5
# str
name = 'Tom'
# bool
is_male = True

# multiple assignment
a, b, c, d = 1, 0.3, 'John', False

# 查看变量类型 type
print(type(x))

# Casting
z = str(x)
print(type(z))
print(z)
