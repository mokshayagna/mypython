def fibonacci(n):
    x=0
    y=1
    print(x,y)
    z=x+y
    while z<=n:
        print(z)
        x=y
        y=z
        z=x+y
fibonacci(20)


