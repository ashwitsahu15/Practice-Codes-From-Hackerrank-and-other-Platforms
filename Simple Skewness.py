def findmean(ps,arr,guess,k,n) :
    if (k == 0) :
        return arr[guess]
    sum0 = (ps[guess+1]-ps[guess-k])+(ps[n]-ps[n-k])
    return sum0/(2*k+1)


n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
ps=[]
s=0
answer=0
for i in range(n) :
    s=s+arr[i]
    ps.append(s)
for guess in range(1,n-1) :
    Rangeofk=min(guess,n-guess-1)

    L=0
    R=Rangeofk
    mid=(L+R)//2

    while R-L>0 :
        currmean=findmean(ps,arr,guess,mid,n)
        k=mid+1
        a=arr[n-k]
        b=arr[guess-k]

        if (a+b)/2 <=currmean :
            R=max(mid,L)
        else :
            L=min(mid+1,R)
        mid=(L+R)//2
    mean=findmean(ps,arr,guess,L,n)
    if (mean-arr[guess]>answer) :
        ans=mean-arr[guess]
        optguess=guess
        optk=L
print((optk*2)+1)
for i in range(optk) :
    print(arr[n-1-i])
for i in range(optk+1) :
    print(arr[optguess-i])



