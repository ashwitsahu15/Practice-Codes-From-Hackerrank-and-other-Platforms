n,q=[int(x) for x in input().split()]
arr=[int(y) for y in input().split()]
for _ in range(q) :
    t,temp=input().split()
    t=int(t)
    temp=int(temp)
    if t==1 :
        arr[temp-1]=1-arr[temp-1]
    elif t==2 :
        arr.sort(reverse=True)
        print(arr[temp-1])