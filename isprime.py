a=25
t=0
for i in range (1,a+1):
    if(a%i==0):
        t=t+1
if(t==2):
    print("is prime")
else:    
     print("is not prime")
