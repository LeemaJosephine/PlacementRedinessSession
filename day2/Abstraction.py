from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    def display(self):
        print("From abstract class")

class CreditCard(Payment):
    def pay(self,amount):
        print("Paid using Credit Card " ,amount)

class UPI(Payment):

    def pay(self,amount):
        print("Paid using UPI " ,amount)

p1 = CreditCard()
p1.pay(100)
p2 = UPI()
p2.pay(100)
p1.display()
p2.display()


