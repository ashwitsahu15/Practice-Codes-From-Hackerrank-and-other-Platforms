ans=0
n=int(input())
value=[int(i) for i in input().split()]
for _ in range(n) :
    ans=ans+value[_]
print(ans)