marks =(90,80,70)
print(marks[0])

# convert tuple to list

temp = list(marks)

# add value to list
temp.append(100)

# convert back to tuple

marks = tuple(temp)

print(marks)

# Tuple concatenation

marks = marks + (200,)
print(marks)
