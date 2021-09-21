n=int(input())
arr=[int(x) for x in input().split()]
k=int(input())
ans=0
for i in range(n-k) :
    j=i+k-1
    if ans==0 :
        ans=sum(arr[i:j+1])
    else :
        ans=max(ans,(ans+arr[j+1]-arr[i-1]))
print(ans)