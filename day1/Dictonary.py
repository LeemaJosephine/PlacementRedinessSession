employee = {
    "name" : "John",
    "age" : 22,
    "role": "Tester"
}

print(employee["name"])

# update
employee["age"] = 26
print(employee["age"])

# delete
del employee["age"]
print(employee)

# add
employee["course"] = "Python"
print(employee)

