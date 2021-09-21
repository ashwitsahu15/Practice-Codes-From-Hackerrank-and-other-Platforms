n=int(input())
k=int(input())
arr=[int(x) for x in input().split()]
i=0
j=k-1
maxi=max(arr[:j+1])
ans=[maxi]*1
while j<n :
    if j-i+1==k :
        
    j+=1
print(ans)