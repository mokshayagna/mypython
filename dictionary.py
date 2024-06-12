a=[
    {"name":"moksha","age":20,"USN":"12345"},
    {"name":"ram", "age":18,"USN":"54321"},
    {"name":"settipalli", "age":19,"USN":"987456"},
    {"name":"saketh", "age":12,"USN":"98745654"}
  ]

b = [
    {"name": "arya", "age": 21, "USN": "67890"},
    {"name": "sita", "age": 19, "USN": "09876"},
    {"name": "prasad", "age": 20, "USN": "456789"},
    {"name": "anil", "age": 13, "USN": "12345678"}
    ]

c = [
    {"name": "vikram", "age": 22, "USN": "112233"},
    {"name": "meera", "age": 20, "USN": "223344"},
    {"name": "rahul", "age": 21, "USN": "334455"},
    {"name": "neha", "age": 14, "USN": "44556677"}
    ]

population=[
            {"name": "vikram", "age": 22, "USN": "112233"},
            {"name": "meera", "age": 20, "USN": "223344"},
           ]
for i in a:
    if i not in population:
        population.append(i)

print(population)


for i in b:
    if i not in population:
        population.append(i)

print(population)

for i in c:
    if i not in population:
        population.append(i)

print(population)