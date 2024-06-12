def is_prime(a):
    t = 0
    for i in range(1,a+1):
        if a % i == 0:
            t = t+ 1
        return t == 2
numbers = [3, 10, 15, 19, 7, 23, 25, 29]
prime = list(filter(is_prime,numbers))