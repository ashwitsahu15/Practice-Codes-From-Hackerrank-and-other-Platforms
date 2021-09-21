n=int(input())
p=int(input())
if p<=(n/2) :
    if p%2==0 :
       ans=(p+1)//2
    else :
        ans=p//2
else :
    ans=(n-p)//2
    if ans==0 and p%2!=0 and n%2==0 :
        ans=ans+1
print(ans)
