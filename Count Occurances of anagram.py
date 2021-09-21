s,t=[x for x in input().split()]
print(s)
n=len(s)
d={}
k=0
ans=0
for i in t :
    if i not in d :
        d[i]=1
    else :
        d[i]+=1
    k+=1
count=len(d)
i,j=0,0
while j<n :
    if s[j] in d :
        d[s[j]]-=1
        if d[s[j]]==0 :
            count-=1
    if j-i+1==k :
        if count==0 :
            ans+=1
        if s[i] in d :
            d[s[i]]+=1
            if d[s[i]]!=0 :
                count+=1
        i+=1
    j+=1
print(ans)
