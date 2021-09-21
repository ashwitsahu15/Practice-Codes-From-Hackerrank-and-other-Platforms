n=int(input())
l=[int(x) for x in input().split()]
l1=[x for x in l if x%2==0]
l2=[x for x in l if x%2!=0]
l1.extend(l2)
print(' '.join(map(str,l1)))



n=int(input())
if n%2!=0 :
    ans=2**((n//2))
else :
    ans=3**((n//2)-1)
print(ans)

