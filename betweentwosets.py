n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
_=a[len(a)-1]
l=[]
ans=[]
while _<=b[0] :
    fact=0
    for j in range(n) :
        if _%a[j]==0 :
            fact+=1
    if fact==len(a) :
        flag=0
        for j in range(m) :
            if b[j]%_==0 :
                flag+=1
        if flag==len(b) :
            ans.append(_)
    _+=1


print(len(ans))