# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0

# for loop
students = ['May', 'Anna', 'Cecilia']
for student in students:
    print(student)

# break continue
for student in students:
    if student == 'Cecilia':
        break
    print(student)

# range
for i in range(10, 15):
    print(i)

# while
count = 0
while count < 10:
    print(count)
    count += 1
