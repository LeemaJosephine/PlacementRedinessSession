def decorator_function(func):

    def wrapper(name):
        print("Before function execution")
        func(name)
        print("After function execution")
    return wrapper

@decorator_function
def display(name):
    print("Welcome to Python ",name)

display("Leema")