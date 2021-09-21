n=int(input())
c=[int(i) for i in input().split()]
jump=0
i=0
while i<n-1 :
    if i+2>=n or c[i+2]==1 :
        i+=1
        jump+=1
    else :
        i+=2
        jump+=1
print(jump)