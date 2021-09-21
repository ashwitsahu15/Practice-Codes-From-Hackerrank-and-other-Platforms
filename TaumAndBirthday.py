t=int(input())
for i in range(t) :
    b,w=[int(i) for i in input().split()]
    bc,wc,z=[int(i) for i in input().split()]
    if abs(wc-bc)>z :
        mini=min(bc,wc)
        if bc>wc :
            conv=b
        else :
            conv=w
        cost=((b+w)*mini)+(z*conv)
    else :
        cost=(b*bc)+(w*wc)
    print(cost)
