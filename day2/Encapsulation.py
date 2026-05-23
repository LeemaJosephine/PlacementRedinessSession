class ATM:
    def __init__(self):
        self.__pin = 0 # private variable

    # Setter method
    def set_pin(self, pin):
        self.__pin = pin

    # Getter method
    def get_pin(self):
        print("PIN:" , self.__pin)

obj = ATM()
obj.set_pin(1234)
obj.get_pin()

