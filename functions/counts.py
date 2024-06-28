input_string = "A2345AA23AAAmnoAwertAAA AAAAAAA 1234AA 1465667AA" 
count = 0
i =0
while i < len(input_string):
    if input_string[i] == 'A' and (i == len(input_string) - 1 or input_string[i+1] != 'A'):
        count = count + 1
    i = i + 1
print(count)   

