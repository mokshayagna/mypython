c = 0
fd = open("moksha.txt","r")
d = fd.readline()
while(len(d)!=0):
    if ("warning" in d):
        c = c + 1
    d=fd.readline()     
print(c)
fd.close()        
