# class Animal:
#
#     # Method overriding
#     def sound(self, name):
#         print("Animal makes sound", name)
#
# class Dog(Animal):
#
#     def sound(self,name):
#         print("Dog Barks", name)
#
# class Cat(Animal):
#     def sound(self,name):
#         print("Cat Meows", name)
#
# c1 = Cat()
# c1.sound('Kitten')
#
# d1 = Dog()
# d1.sound('Puppy')

# Method Overloading
#
# class Calculator:
#
#     def add(self,a,b=0,c=0):
#         print(a+b+c)
#
# obj = Calculator()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# Operator Overloading

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(80)
s2 = Student(90)

print(s1 + s2)