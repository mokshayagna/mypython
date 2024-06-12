def main():
    n=5
    m=5
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end="")
        for k in range(1,m+1):
         print(k,end="")
        m=m-1
        print()

if(__name__ == "__main__"):
    main()