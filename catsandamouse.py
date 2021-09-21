q=int(input())
for _ in range(q) :
    x,y,z=[int(i) for i in input().split()]
    if abs(x-z)<abs(y-z) :
        print('Cat A')
    elif abs(y-z)<abs(x-z) :
        print('Cat B')
    else :
        print('Mouse C')
