engineers = ['Saketh', 'Jana', 'Vachan', 'Aura']
programmers = ['Vachan', 'Sama', 'Dheer', 'Aura', 'Achyu']
managers = ['Jana', 'Vachan', 'Dheer', 'Achyu']
engineers.extend(programmers + managers)
new_list = []
for person in engineers:
    if person not in new_list:
        new_list.append(person)

print(new_list)
