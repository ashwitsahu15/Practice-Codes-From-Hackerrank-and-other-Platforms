s=list(input())
t=list(input())
k=int(input())
for i in range(min(len(s),len(t))) :
    if s[i]!=t[i] :
        lead=i
        break
    else :
        lead=i+1

temp=len(s)+len(t)-(2*lead)

if k>=len(s)+len(t) :
    print('Yes')
elif temp<=k and (temp%2)==(k%2):
    print('Yes')
else :
    print('No')
