n=int(input())
arr=[int(i) for i in input().split()]
identical=set(arr)
identical=list(identical)
maxi=0
for _ in range(len(identical)) :
    value=arr.count(identical[_])
    if value>maxi :
        maxi=value
        ans=identical[_]
    elif value==maxi :
        if identical[_-1]<identical[_] :
            ans=identical[_-1]
        else :
            ans=identical[_]
print(ans)