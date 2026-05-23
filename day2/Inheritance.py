# Hierarchical Inheritance
class Father:
    def house(self):
        print("2BHK")

class Child1(Father):
    def money(self):
        print("Money")

class Child2(Father):
    def bike(self):
        print("Ntorq")

obj = Child1()
obj.house()
obj.money()

obj1 = Child2()
obj1.bike()
obj1.house()