s=input()
s=list(s)
a=[]
count=1
for i in range(len(s)-1) :
    print(s[i],s[i+1])
    if s[i]==s[i+1] :
        count+=1
    else :
        a.append(s[i])
        a.append(count)
        count=1
a.append(s[-1])
a.append(count)
print(*a,sep='')