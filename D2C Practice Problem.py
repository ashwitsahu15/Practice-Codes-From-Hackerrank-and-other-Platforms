n=int(input())
s,q=input().split()
q=int(q)
for _ in range(q) :
    a,b=[int(x) for x in input().split()]
    count=0
    flag=0
    arr=s[a:b+1]
    d={}
    for i in arr :
        if i not in d :
            d[i]=1
        else :
            d[i]+=1
    for j in d :
        if d[j]%2!=0 :
            flag+=1
    if flag>1 :
        arr=list(arr)
        arr.sort()
        arr=''.join(arr)
        print(s[:a]+arr+s[b+1:])
    else :
        