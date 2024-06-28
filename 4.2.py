import pdb

a = [2, 3, 2, 5, 5, 7, 8, 1, 1]
n = len(a)
i = 0

#pdb.set_trace()

while i < n:
    j = i + 1
    while j < n:
        if(a[i]==a[j]):
            del(a[j])
            n = n - 1
        j = j + 1
    i = i + 1

for i in range(n):
    print(a[i], end = " ")
print()


# list
# print(i, j, a)
# display(i)
# continue
# step
# next
#quit