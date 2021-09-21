p,d,m,s=[int(x) for x in input().split()]
if p>d :
    flag=0
    while s>0 :
        flag+=1
        s-=p
        if p<=m :
            p=m
        else :
            p=p-d
    print(flag-1)
else :
    flag=s//m
    print(flag)

