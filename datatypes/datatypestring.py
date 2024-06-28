# %d %c %s %f %r
# Mutable   - Modifyable 
# Immutable - Can't Modify
# Strings

def strings_printing():
    test_str = "Aura Networks Bangalore"
    print (test_str)
    print ("String is    :",test_str)
    print ("String is    :%s" % (test_str))
    print (f"String is   :{test_str}")
    print ( "String is   :{test_str}")
    print()

    print(len(test_str))
    print(f"Length of test_str is :{len(test_str)}")
    print()

    print(test_str)
    print(f"First  byte :{test_str[0]}")
    print(f"Second byte :{test_str[1]}")
    print()

    i = 0
    while (i < len(test_str)):
        print(test_str[i], end=" ")
        i += 1
    print()

    for temp in test_str:
        print(temp, end=" ")

    print()
    return

def string_properties_1():
    a = 10
    print(a)
    a = a + 1
    print(a)

    test_str = "Aura Networks Bangalore"
    # This is NOT possible
    # test_str[2] = 'R'
    print(test_str[2])
    print(test_str)

    #This is possible
    test_str = "Aura Networks Amaravathi"
    print(test_str)
    return

def string_slice_n_dice():
    test_str = "Aura Networks Bangalore"
    print(f"     :{test_str}")
    print(f" 0   :{test_str[0]}")
    print(f" 1   :{test_str[1]}")
    print(f"-1   :{test_str[-1]}")
    print(f"-2   :{test_str[-2]}")
    print(f" 1:6 :{test_str[1:6]}")
    print(f" 1:23:{test_str[1:23]}")
    print(f" 1:30:{test_str[1:30]}")
    print(f" 0:30:{test_str[0:30]}")
    print(f" ':' :{test_str[:]}")
    print(f"5:   :{test_str[5:]}")
    print(f"':-1':{test_str[:-1]}")
    print(f"-2:  :{test_str[-2:]}")
    # test_str[<sp>:<ep>:<order>]
    print(test_str[::-1])
    print(test_str[::])
    print(test_str[13:-1])
    print(test_str[:13:-1])
    print(test_str[5::1])
    print(test_str[5::2])
    print(test_str[5::3])

def string_printing_2():
    name = "Saketh Ram"
    age = 14
    salary = 1000
    height = 5.123

    print (name, age, salary, height)
    print ("my friend", name, "age is", age, "and salary is", salary, "height is", height)
    print ("my friend %s age is %d and salary is %d height is %f" % (name, age, salary, height))
    print ("%s xxxxxx %d yyyyyyyy %d zzzzzzz %f" % (name, age, salary, height))
    print (f"my friend {name} age is {age} and salary is {salary} height is {height}")

    print(name, age)
    print(age * 3)
    print(height * 3)
    print(name * 3)
    print(str(height) * 3)
    a = '10'
    print(int(a))

    a = 'Aura10'
    print(int(a))

    s = "Aurovill"
    s = "B" + s[:]
    print(s)

    s = "Aurovill"
    s = "B" + s[2:]
    print(s)

    s = "Aurovill"
    s = "B" + s[2:5]

    s = "Aurovill"
    s = "B" + s[1:5]
    print (s)
    return


def string_functions_intro():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f"sou              : {sou}")
    print(f"sou.capitalize() : {sou.capitalize()}")
    print(f"sou              : {sou}")

    sou = sou.capitalize()
    print(f"sou              : {sou}")

def string_help():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(dir(sou))
    print("")

    print(dir(""))
    # help(sou.capitalize)
    # help("".capitalize)
    # help(sou.count)

    a = 10
    print(dir(a))
    return

def string_functions_1():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f"sou                  : {sou}")
    sub = "i"
    
    print(f"sou.len()             :{len(sou)}")
    print(f"sou.count(sub)        :{sou.count(sub)}")
    print(f"sou.count(sub, 30)    :{sou.count(sub, 30)}")
    print(f"sou.count(sub, 30, 50):{sou.count(sub, 30, 50)}")
    print("")

    sub = "India"
    print(f"sou.count({sub})       :{sou.count(sub)}")

    sub = " "
    print(f"sou.count({sub})       :{sou.count(sub)}")

    sub = "unity"
    print(f"sou.count({sub})       :{sou.count(sub)}")

def string_functions_2():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f"sou  :{sou}")
    prefix = "World"
    suffix = "Patel"
    print(f"1. :{sou.endswith(suffix)}")
    print(f"2. :{sou.endswith(suffix, 5, 10)}")
    print(f"3. :{sou.startswith(prefix)}")
    print(f"4. :{sou.capitalize()}")
    print(f"5. :{sou.capitalize().startswith(prefix)}")

    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel   "
    print(f"6. :{sou.count('a')}")
    print(f"7. :{'   '.count('a')}")

    print("")
    return 

def string_find_index():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    substr = "tallest"
    print(f"1. :{sou.find(substr)}")
    print(f"2. :{sou.find(substr, 5)}")
    print(f"3. :{sou.find(substr, 20)}")
    print(f"4. :{sou.find('india')}")
    print(f"5. :{sou.index(substr)}")
    print(f"6. :{sou.index(substr, 5)}")
    print(f"7. :{sou.index(substr, 20)}")
    print("")

def string_functions_3():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f"1. :{sou.islower()}")
    print(f"2. :{sou.lower()}")
    print(f"3. :{sou.lower().islower()}")

    print("")
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f"1. :{sou.isupper()}")
    print(f"2. :{sou.upper()}")
    print(f"3. :{sou.upper().capitalize()}")
    print(f"4. :{sou.upper().capitalize().islower()}")
    print(f"5. :{sou.upper().isupper()}")
    # print(f"5. :{sou.isupper().upper()}")
    
    retval = sou.isupper()
    print(type(retval))
    print(dir(retval))

    print("")

    sou = "      "
    print(sou.isspace())

    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(sou.isspace())

    print("")

def string_replace():
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(sou)
    print(sou.replace("ll", "LL"))
    print(sou)

    print("")
    sou = "worlds tallest Statue of Unity 597f, Vallabhbhai Patel"
    print(f'1. :{sou.replace("ll", "LL")}')
    print(f'2. :{sou.replace("ll", "LL", 1)}')  #Number of occurences to replace
    print(f'3. :{sou.replace("ll", "LL", 2)}')  #Number of occurences to replace
    print(f'4. :{sou[20:].replace("ll", "LL")}') 
    print("")
    return

#rstrip, lstrip, strip
def string_strip():
    sou = "       worlds tallest Statue of Unity 597f,     Vallabhbhai Patel    "
    print("1. %s" % sou)
    print("1. %d" % len(sou))

    #rstrip lstrip strip
    print(f"2. {sou.rstrip()}")
    print(f"2. {len(sou.rstrip())}")

    print(f"3. {sou.lstrip()}")
    print(f"3. {len(sou.lstrip())}")

    print(f"4. {sou.strip()}")
    print(f"4. {len(sou.strip())}")

    print("")

    sou = "IIIIIIIworlds tallest Statue of Unity 597f,     Vallabhbhai PatelIIIIII"
    print(sou)
    print(sou.rstrip('I'))
    print(sou.rstrip('I').lstrip('I'))
    print(sou.rstrip('I').lstrip('I').lstrip("wo"))
    print(sou.strip('I'))

    sou = "IIIIIIIworlds tallest Statue of Unity 597f,    VallabhbhaiIIIIIPatelIIIIII"
    #output should be sou = "worlds tallest Statue of Unity 597f,    Vallabhbhai Patel";
    print(sou)
    substr = "Patel"
    print(sou.strip('I'))
    print(sou.lstrip('I').rstrip('I').rstrip(substr).rstrip('I')+substr)
    return

def string_split():
    #String with tabs, single space and multiple spaces
    phnum = "         970 2096   756             "
    print(phnum)
    print(phnum.split())
    print(phnum.split()[1])
    print("".join(phnum.split()))
    
    print("-".join(phnum.split()))
    print(" ".join(phnum.split()))
    print(phnum)

    tstr = "     Aura Networks     Bengaluru   "
    print(" ".join(tstr.split()))

    print("")
    tstr = "     Aura Networks  \nBengaluru\nIndia  "
    print(tstr)
    print(tstr.split())
    print(tstr.split(' '))
    print(tstr.split(' ', 1))
    print(tstr.split(' ', 2))
    print(tstr.split('\n'))

    print("")
    email = "bhagavanprasad@gmail.com"
    print(email)
    print(email.split('@'))

    username = email.split('@')[0]
    dname = email.split('@')[1]
    print(username)
    print(dname)

    a, b = [10, 20]
    username, dname = email.split('@')
    print(username)
    print(dname)
    return

def main():
    # strings_printing()
    # string_properties_1()
    # string_slice_n_dice()
    # string_printing_2()  
    # string_functions_intro()
    # string_help()
   #  string_functions_1()
    string_functions_2()
    #string_find_index ()
    # string_functions_3()
    # string_replace()
    # string_strip()
    #string_split()
    return

if __name__ == "__main__":
    main()
    