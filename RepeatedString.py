s=input()
n=int(input())
ans=int((n/len(s)))*s.count('a')
for i in range(n%len(s)) :
    if s[i]=='a':
        ans+=1
print(ans)
