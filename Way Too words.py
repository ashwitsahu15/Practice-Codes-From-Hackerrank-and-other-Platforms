for _ in range(int(input())) :
    s=input()
    l=len(s)
    if l>10 :
        l=l-2
        print(s[0]+str(l)+s[-1])
    else :
        print(s)