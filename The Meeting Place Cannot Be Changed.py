n=int(input())
distance=[int(x) for x in input().split()]
speed=[int(x) for x in input().split()]
def position(t) :
    right=max([distance[i]-(speed[i]*t) for i in range(n)])
    left=min([distance[i]+(speed[i]*t) for i in range(n)])
    return right>left
L,R=0,1e9
while abs(R-L)>1e-6 :
    ans=(L+R)/2
    if position(ans) :
        L=ans
    else :
        R=ans
print(ans)