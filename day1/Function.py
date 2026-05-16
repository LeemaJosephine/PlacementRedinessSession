def greet():
    print("Hello")
greet()

def add(a,b):
    print(a+b)
add(1,2)

def sub(a,b):
    return a-b

result = sub(1,2)
print(result)

# Lambda Function

print("Lambda Function")

square = lambda x : x*x
print(square(10))

result=lambda a,b : a + b
print(result(1,2))

print("Map Function")

numbers = [1,2,3,4,5,6,7,8,9]

result = list(map(lambda x : x*2,numbers))
print(result)

names = ["John","Bob","Jane"]

result = list(map(str.upper,names))
print(result)

print("Filter Function")
numbers = [1,2,3,4,5,6,7,8,9]

even=list(filter(lambda x : x%2==0, numbers))
print(even)