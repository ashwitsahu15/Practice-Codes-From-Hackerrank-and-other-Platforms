l=int(input())
a=[int(x) for x in input().split()]
i=0
while i<len(a)-1 :
    if a[i]==a[i+1] :
        a[i]+=1
        a.remove(a[i+1])
        i=0
    else :
        i+=1
print(len(a))