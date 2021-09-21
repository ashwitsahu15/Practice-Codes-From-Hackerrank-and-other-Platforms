n=int(input())
arr=[int(_) for _ in input().split()]
maxi=max(arr)
ans=0
for _ in arr :
    if _==maxi :
        ans+=1
print(ans)