n=int(input())
shared=5
ans=0
for i in range(n) :
    liked=int(shared/2)
    shared=liked*3
    ans+=liked
print(ans)