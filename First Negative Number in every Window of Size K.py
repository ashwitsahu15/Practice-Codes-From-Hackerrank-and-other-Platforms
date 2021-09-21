n=int(input())
k=int(input())
arr=[int(x) for x in input().split()]
ans=[]
neg=[]
j=0
i=0
while j<n :
    if arr[j]<0 and arr[j] not in neg:
        neg.append(arr[j])
    if j-i+1==k :
        if len(neg)>0 : 
            print(arr[i],neg)
            if arr[i]!=neg[0] :
                ans.append(neg[0])
            elif arr[i]==neg[0] :
                ans.append(neg[0])
                neg.pop(0)
        else :
            ans.append(0)
        i+=1
    j+=1
print(*ans,sep=' ')
     