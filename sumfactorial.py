n=5
sum=0
for a in range(1,n+1):
    f=1
    for i in range(1,a+1):
        f=f*i
    sum=sum+f
print(sum)