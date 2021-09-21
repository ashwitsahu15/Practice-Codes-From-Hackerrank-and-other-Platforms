import math

for _ in range(int(input())) :
    n,s=[int(x) for x in input().split()]
    x=math.ceil(n/2)
    print(x)
    n-=(x-1)
    print(s//n)