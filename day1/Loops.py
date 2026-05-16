# Print numbers 1 to 10

for i in range(1,11):  # < 11
    print(i)

# print even numbers
print("Even Numbers!")
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# Sum of Numbers
print("Sum of numbers!")
total = 0
for i in range(1,6):
    total += i

print(total)

# pattern program

for i in range(1,6):
    print("*"*i)  ## -> 1, 2

print("Print numbers using while loop")

count =1

while count <=10: # as long as condition is true loop will be executed
    print(count)
    count +=1

