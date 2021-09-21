t=int(input())
for _ in range(t) :
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    length=[x for x in a if x<=0]
    if len(length)>=k :
        print('NO')
    else :
        print('YES')