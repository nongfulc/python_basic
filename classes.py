# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0
# A class is like a blueprint of creating objects. An Object has properties and functions.
# create class
class Person:
    # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def say_hello(self):
        print(f'my name is {self.name}')


# Init person
joe = Person('Joe', 29, 'joe@gmail.com')
print(type(joe))
print(joe.name)
joe.say_hello()


# extend class
class Student(Person):
    def __init__(self, student_id, name, age, email):
        super().__init__(name, age, email)
        self.student_id = student_id

    # def say_hello(self):
    #     print(f'my student id is {self.student_id}')


student_mary = Student(1, 'Mary', 17, 'mary@gmail.com')
print(student_mary.student_id)
student_mary.say_hello()
