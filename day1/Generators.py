def number():
    return [1,2,3]
print(number())

def numbers():
    for i in range(1,6):
        yield i

for value in numbers():
    print(value)