for T in range(int(input())) :
    n,c,m=[int(x) for x in input().split()]
    ans=n/c
    w=ans
    while(w>=m) :
        temp=w%m
        w=int(w/m)
        ans+=w
        w=temp+w
    print(int(ans))