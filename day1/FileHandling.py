# create and write in file
file = open("demo.txt","w")
file.write("Welcome to Python!")
file.close()

# Append file - add extra lines

file = open("demo.txt","a")
file.write(" Hello World!")
file.close()

# reading the file
try:
    file = open("demo.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
file.close()

