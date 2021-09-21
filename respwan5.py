n=int(input())
ans=n+n-1
n=ans
for i in range(n) :
    if i%2!=0 :
        print(i)
        ans+=(2*i)
print(ans)