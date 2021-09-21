t=int(input())
for _ in range(t) :
    n,m,s=[int(i) for i in input().split()]
    if s+m-1 > n :
        if (s+m-1)%n==0 :
            print(n)
        else :
            print((s+m-1)%n)
    else :
        print(s+m-1)