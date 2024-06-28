combined_number1 = 0
for i in range(len(l1)):
    combined_number1 = combined_number1 * 10 + l1[i]
a = combined_number1
b1 = 0
while a > 0:
    b1 = (b1 * 10) + (a % 10)
    a = a // 10
print(b1)
combined_number2 = 0
for i in range(len(l2)):
    combined_number2 = combined_number2 * 10 + l2[i]
a = combined_number2
b2 = 0
while a > 0:
    b2 = (b2 * 10) + (a % 10)
    a = a // 10
print(b2)
c = b1 + b2
b = 0
while c > 0:
    b = (b * 10) + (c % 10)
    c = c // 10
print(b)