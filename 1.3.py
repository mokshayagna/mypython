a=626
c = a
b=0
while a>0:
    b=(b*10)+(a%10)
    a=a//10
if(c == b):
    print("is palindrome")
else:
    print("is not palindrome")
