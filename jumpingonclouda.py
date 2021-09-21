n,k=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
e=100
i=0
while ((i+k)%n)!=0 :
    e-=1
    i=(i+k)%n
    if c[i]==1 :
        e-=2
if ((i+k)%n)==0 :
    e-=1
    if c[0]==1 :
        e-=2 
print(e)