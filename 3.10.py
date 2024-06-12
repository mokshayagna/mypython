def main():
    n=5
    m=5
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(j,end = "")
        m=m-1
        print()

if(__name__ == "__main__"):
    main()