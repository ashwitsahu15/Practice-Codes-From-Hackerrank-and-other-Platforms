n,k=[int(i) for i in input().split()]
ar=[int(i) for i in input().split()]
t=(n*(n-1)/2)
flag=0
temp=1
i=0
while t>0 :
    while i<n-1 :
        for j in range(temp,n) :
            pair=[]
            pair.append(ar[i])
            pair.append(ar[j])
            if sum(pair)%k==0 :
                flag+=1
        temp+=1
        i+=1
    t-=1
print(flag)