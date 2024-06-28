n = 5
i = 0
j = n//2
# a=[
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
# ]
a=[[0 for i in range(n)]for j in range(n)] 
for num in range(1,n*n+1):
    a[i][j] = num
    i = i - 1
    j = j + 1
    if i < 0 and j >= n:
        i = i + 2
        j = j - 1
    elif i < 0:
        i = n - 1
    elif j >= n:
        j = 0
    elif a[i][j] != 0:
        i = i +2
        j = j - 1
for i in range (0,n):
    for j in range (0,n):
        print(a[i][j], end = "   ")
    print()
print()