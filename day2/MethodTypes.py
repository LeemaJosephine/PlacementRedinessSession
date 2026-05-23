class Student:

    school_name="ABC school"

    def __init__(self,name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Instance Method
    def displayName(self):
        print("Welcome to the school " , self.name)

    @staticmethod
    def add(a,b):
        return a + b


# Calling class method
Student.change_school("XYZ School")
print(Student.school_name)

# Creating object to execute the instance method
obj = Student("NMN School")
obj.displayName()

# Calling the static method
result = Student.add(1,2)
print(result)