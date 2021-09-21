import math

s=input()
s="".join([str(x) for x in s if x!=" "])
l=len(s)
r=math.floor((len(s)**(1/2))) 
c=math.ceil((len(s)**(1/2))) 
if r*c<l :
    r=max(r,c)
    c=r
temp=c
ans=[]
finalans=[]
x=0

for i in range(r) :
    ans.append(s[x:c])
    x+=temp
    c+=temp
for j in range(temp) :
    final=[]
    for _ in ans :
        try :
            final.append(_[j])
        except :
            pass
    finalans.append("".join(final))

print(" ".join(finalans))