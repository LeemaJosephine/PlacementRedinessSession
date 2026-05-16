from operator import index

company ="Automation"

print(company[0])
print(company[-1])
print(company[0:5])  # range

print(company.upper())
print(company.lower())
print(company.replace("Auto","Demo"))

print(len(company))

## print reverse

print(company[::-1])

# print reverse using loop

reverse =""

for char in company:
    reverse = char + reverse # m+otuA

print(reverse)


text ="python"

#text[0] = 'j' -> Error

new_text = "j" + text[1:]
print(text)
print(new_text)

a = 10
b = a
a = 20

print(b)