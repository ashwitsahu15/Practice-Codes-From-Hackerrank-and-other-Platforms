t=int(input())
while(t) :
    n=int(input())
    s=input()
    flag=False
    if s.count('a')==s.count('b') :
        print(1,n)
        flag=True
    else :
        for i in range(1,n) :
            d=s[i:]
            if d.count('a')==d.count('b') :
                print(i+1,n)
                flag=True
                break
    if (flag==False) :
        print(-1,-1)
    t-=1