a = [2,3,2,5,5,7,8,1,1]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            a[j] = 0
for i in range(0,len(a)):
    print(a[i],end="")
print()
