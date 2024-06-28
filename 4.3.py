a = [5, 2, 1, 3, ]
i = 0
n = len(a)
while i < n:
    j = i + 1
    while j < n:
        if a[i] > a[j]:
            b    = a[i]
            a[i] = a[j]
            a[j] = b
        j = j + 1
    i = i + 1
for i in range (len(a)):
    print(a[i],end = "")
print()