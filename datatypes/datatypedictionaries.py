def dictionaries_purpose():
    linfo = ["LakshmiPathi", "Python", 100, "Hindi"]
    dinfo = {"name":"LakshmiPathi", "course":"Python", "id":100, "canspeak":"Hindi"}
    # json - Java Script Object Notation

def dict_basics():
    atomic_elements = {
        "H": "hydrogen",
        "He": "helium",
        "Li": "lithium",
        "C": "carbon",
        "O": "oxygen",
        "P": "phosp",
        "N": "nitrogen"
    }

    print(atomic_elements)
    print(atomic_elements["C"])
    print(atomic_elements["O"])
    # print(atomic_elements["o"])
    print("")

    print("O" in atomic_elements)
    print("o" in atomic_elements)
  
    if ("O" in atomic_elements):
        print("'O' Key is available")
        print(atomic_elements["O"])

    if ("U" in atomic_elements):
        print("'U' Key is available")
    else:
        print("'U' Key is NOT available")

    print("oxygen" in atomic_elements)
    print(atomic_elements.get("P", "The item 'P' Not available"))
    print(atomic_elements.get("c", "The item 'c' Not available"))
    atomic_elements.update( {"B": "Bromium"} )
    atomic_elements.update( {"P": "Phosphorous", "S": "Sulfur"} )
    print(f"1:{atomic_elements}")

    del atomic_elements['C']
    print(atomic_elements)
    # print (atomic_elements["C"])
    return

def dict_operations():
    atomic_elements = {
        "H": "hydrogen",
        "He": "helium",
        "Li": "lithium",
        "C": "carbon",
        "O": "oxygen",
        "P": "phosp",
        "N": "nitrogen"
    }
    print(atomic_elements.keys())
    print(list(atomic_elements.keys()))
    print(list(atomic_elements.values()))
    print(list(atomic_elements.items()))

    print("")
    
def little_complex_dict():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'phone': ['9902000000', '900000000']}
    
    print("dict['Name']: ",  dict['Name'])
    print("dict['Age']: ",   dict['Age'])
    print("dict['Class']: ", dict['Class'])
    print("dict['phone']: ", dict['phone'])
    print("dict['phone']: ", dict['phone'][1])
    print("dict['phone']: ", dict['phone'][0][0])

    print(type(dict))

def dict_with_diff_key_types_1():
    atomic_number_to_name = {
        1: "hydrogen",
        6: "carbon",
        7: "nitrogen",
        8: "oxygen",
        "8": "OXYGEN"
    }

    print(atomic_number_to_name)
    print(atomic_number_to_name[1])
    print(atomic_number_to_name[8])
    print(atomic_number_to_name["8"])
    # print(atomic_number_to_name[3])
    print(atomic_number_to_name.items())

def dict_with_diff_key_types_2():
    nobel_prize_winners = {
        (1913, "Literature"): "Rabindranath Tagore",
        (1928, "Physics"): "Sir. CV Raman",
        (1979, "physics"): ["Glashow", "Salam", "Weinberg"],
        # [1979, "physics"]: ["Glashow", "Salam", "Weinberg"],
    }

    print(nobel_prize_winners[(1913, "Literature")])
    # print(nobel_prize_winners[(1913)])

def making_it_more_complex():
    states = {
        'Andhra Pradesh': 'AP',
        'Karnataka': 'KA',
        'Telangana': 'TS',
        'Tamilnadu': 'TN',
        'Gujarath': 'GJ',
        'Maharashtra': 'MH'
    }

    cities = {
        'MH': 'Mumbai',
        'AP': 'Amaravathi',
        'TS': 'Hyderabad',
        'TN': 'Chennai',
        'KA': 'Bengaluru'
    }

    print(states)
    print(cities)
    
    states['Odisha'] = 'OR'
    print(states)

    cities['OR'] = 'Bhuvaneswar'
    cities['GJ'] = 'Gandhinagar'

    print(states)
    print(cities)
    
    print('-' * 10)
    print("MH State has: ", cities['MH'])
    print("OR State has: ", cities['OR'])

    print('-' * 10)
    print("Karnataka's abbreviation is      : ", states['Karnataka'])
    print("Maharashtra's abbreviation is    : ", states['Maharashtra'])
    print("Andhra Pradesh's abbreviation is : ", states['Andhra Pradesh'])

    # do it by using the state then cities dict
    print('-' * 10)
    print("Maharashtra has: ", cities[states['Maharashtra']])
    print("Gurarath has: ",    cities[states['Gujarath']])

    print('-' * 10)
    print(states.items())

    for temp in list(states.items()):
        print (temp)
    t = ('10', 20)
    a, b = t
    print(a, b)

    for state, abbrev in list(states.items()):
        print("'%-15s' is abbreviated '%s'" % (state, abbrev))

    # print every city in state
    print('-' * 10)
    for abbrev, city in list(cities.items()):
        print("'%s' has the city '%s'" % (abbrev, city))

    # now do both at the same time
    print('-' * 10)
    for state, abbrev in list(states.items()):
        print("'%-15s' state is abbreviated '%s' and has city '%s'" % (state, abbrev, cities[abbrev]))
    
    print('-' * 10)

    # print (states['Kerala'])

    # safely get a abbreviation by state that might not be there
    state = states.get('Kerala')
    print(state)
    if not state:
        print("Sorry, no Kerala.")

    # get a city with a default value
    city = cities.get('KR', 'Does Not Exist')
    print(f"The city for the state 'KR' is: {city}")
    return

def missalenious_dict():
    my_dict = {'Name': 'Aura', 'Age': 5, 'Location': 'Bangalore'}
    print(my_dict)
    my_dict.clear()   
    print(my_dict)
    
    del my_dict     
    # print (my_dict)

    # empty dictionary
    my_dict = {}
    print(my_dict)

    my_dict = dict()
    print(my_dict)

    return    

def main():
    # dictionaries_purpose()
    dict_basics()
    # dict_operations()
    # little_complex_dict()
    # dict_with_diff_key_types_1()
    # dict_with_diff_key_types_2()
    # making_it_more_complex()
    # missalenious_dict()
    return

if __name__ == "__main__":
    main()