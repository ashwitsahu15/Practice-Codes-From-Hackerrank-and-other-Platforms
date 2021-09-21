for T in range(int(input())) :
    n,k,p,q=[int(x) for x in input().split()]
    ans=min(n-1,(abs(p-q))+k)
    print(ans)
