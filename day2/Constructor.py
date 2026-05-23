class Student:

    # def __init__(self):
    #     print("Constructor called")

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayName(self):
        print("Hello " + self.name)
        print("Your age" , self.age)

obj = Student("John",18)
obj.displayName()