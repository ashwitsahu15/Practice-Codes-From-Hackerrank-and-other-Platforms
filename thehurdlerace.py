n,k=[int(i) for i in input().split()]
height=[int(i) for i in input().split()]
maxi=max(height)
ans=maxi-k
if ans>0 :
    print(ans)
else :
    print(0)