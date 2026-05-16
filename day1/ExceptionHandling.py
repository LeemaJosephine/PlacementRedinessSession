try:
    num = 10 /2
    print(num)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Something went wrong")

finally:
    print("Closing program")