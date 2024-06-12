def list_basics():
    poets = ["kuvempu", "vemana", "kamala", "Kalidas"]

    print(poets)
    print('_' * 10)
    poets.append("cinarey")
    
    poets.append("10")
    
    poets.append("10")
    
    poets.append(10)
   

    print(poets)
    print('_' * 10)

    poets.reverse()
    print(poets)
    print('_' * 10)

    del poets[0]
    print(poets)

    poets.sort()
    print(poets)
    print('_' * 10)

    poets.sort(reverse=True)
    print(poets)
    print('_' * 10)

    poets.insert(2, "Thiruvalluvar")
    print(poets)
    print('_' * 10)
    poets.insert(10, "Thiruvalluvar")
    print(poets)
    return

def list_operations_01():
    subjects = ['physics', 'chemistry', '1997', '2000']
    numbers = [1, 2, 3, 2, 5, 2, 5, 2 ]
    print(f"subjects[0]  :{subjects[0]}")
    print(f"numbers[1:5] :{numbers[1:5]}")

    print(subjects[2])
    subjects[2] = 2001
    print(subjects)

    print(numbers)
    print(numbers.count(2))
    print(numbers.count(1))
    print(numbers.count(10))
    print(len(numbers))

    #print(f"subjects: {subjects}")
    #print(f"numbers: {numbers}")
    subjects.extend(numbers) #this adds all numbers elements to subjects
    print(f"subjects: {subjects}")
    print(f"numbers: {numbers}")
    # subjects.sort()
    print(f"subjects: {subjects}")
    return

def list_operations_02():
    subjects = ['physics', 'chemistry', '1997', '2000']
    numbers = [1, 2, 3, 2, 5, 2, 5, 2 ]
    print(subjects.index('chemistry'))
    print(subjects.index('physics'))
    # print(subjects.index('maths'))

    print(f"numbers: {numbers}")
    print(numbers.pop())
    print(f"numbers: {numbers}")
    print(numbers.pop(-1))
    print(f"numbers: {numbers}")

    print(numbers.pop(2))
    print(f"numbers: {numbers}")
    numbers.pop(2)
    print(f"numbers: {numbers}")



def list_operations_03():
    subjects = ['physics', 'the subject english is', 'chemistry', '1997', 2000]

    new_sub = "maths"
    print(f"1 : {new_sub in subjects}")
    if (new_sub in subjects):
        print("Found")
    else:
        print("Appending")
        subjects.append(new_sub)

    print(subjects)

    new_sub = "english"
    if (new_sub not in subjects):
        print("Appending")
        subjects.append(new_sub)

    print(subjects)

    for x in "Aura Bengaluru":
        print (x)

    for x in "Aura Bengaluru", 123:
        print (x)

    for x in 123:
        print (x)

    subjects = ['physics', 'the subject english is', 'chemistry', '1997', '2000']
    for x in subjects:
        print (x)

    return










def main():
    list_basics()
   # list_operations_01()
    #list_operations_02()
   # list_operations_03()
    return

if __name__ == "__main__":
    main()