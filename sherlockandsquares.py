import math
def CountSquares(a, b): 
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

q=int(input())
for i in range(q) :
    a,b=[int(i) for i in input().split()]
    print(int(CountSquares(a,b)))
