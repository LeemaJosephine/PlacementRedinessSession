class Student: # class

    name="John"  # Variable

    def displayName(self):  # Function
        print("Hello "+ self.name)

obj = Student()  # Object creation
obj.displayName()  # Calling function using object
print(obj.name) # Calling variable using object

# Python internally converts it to

# Student.display(obj)
