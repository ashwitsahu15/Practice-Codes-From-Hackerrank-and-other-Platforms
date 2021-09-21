for T in range(int(input())) :
    n=int(input())
    a=[bin(x) for x in range(1,n+1)]
    print(a)
    for i in a :
        s=i
        for j in range(len(s)-1) :
            if s[j]=='1' and s[j+1]=='1' :
                a.remove(s)
    print(len(a))
    