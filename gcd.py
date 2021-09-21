# m,n=[int(x) for x in input().split()]
# mini=min(m,n)
# while mini>0 :
#     if m%mini==0 and n%mini==0 :
#         print(mini)
#         break
#     mini-=1


# By Eucild's Algorithm

m,n=[int(x) for x in input().split()]
def gcd(m,n) :
    if m<n :
        m,n=n,m
    
    if m%n==0 :
        return n
    else :
        return gcd(n,m%n)
print(gcd(m,n))