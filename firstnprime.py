n=20
for a in range(1,n+1):
    t=0
    for i in range(1,n+1):
        if(a%i==0):
            t=t+1
    if(t==2):
         print(a)
