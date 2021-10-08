# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/4
# @Version 1.0
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate memebers.
person = {
    'name': 'LC',
    'age': 29
}

# Constructor
person2 = dict(name='Anna', age=29)

print(person2)
print(person)
# get value
print(person.get('name'))
print(person['age'])

# add key/value
person['hometown'] = 'China'
print(person.get('hometown'))

# Get dict items
print(person.items())

# Copy
person3 = person.copy()
person3['name'] = 'John'
print(person)
print(person3)

# remove items
person.pop('name')
del (person['age'])
print(person)

# len
print(len(person))
