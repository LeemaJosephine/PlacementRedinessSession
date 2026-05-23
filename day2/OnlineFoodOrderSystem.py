import re

# Parent Class
class Resturant:

    def show_menu(self):
        print("----- MENU -----")
        print("1. Pizza - 250")
        print("2. Burger - 150")
        print("3. Shawarma - 200")
        print("4. Fried Rice - 180")

# Child class
class Customer(Resturant):

    def __init__(self,name,phone):
        self.name = name

        # Encapsulation
        self.__phone = phone

    def validate_phone(self):

        pattern = r"^[6-9]\d{9}$"

        if re.match(pattern,self.__phone):
            return True
        else:
            return False

    # Display customer deatils
    def customer_details(self):

        print("----- Customer Details -----")
        print("Customer Name: " + self.name)
        print("Phone Number: " + self.__phone)

    #Place order
    def place_order(self):

        self.show_menu()

        choice = int(input("Enter item number: "))

        if choice == 1:
            print("Pizza - ordered successfully")

        elif choice == 2:
            print("Burger - ordered successfully")

        elif choice == 3:
            print("Shawarma - ordered successfully")

        elif choice == 4:
            print("Fried Rice - ordered successfully")

        else:
            print("Invalid choice")

#Main Program
name = input("Enter customer name: ")
phone = input("Enter mobile number: ")

customer1 = Customer(name,phone)

# Validate the phone
if customer1.validate_phone():
    print("\nMobile Number Validated Successfully")
    customer1.customer_details()
    customer1.place_order()
else:
    print("\nInvalid Mobile Number")