n,q=[int(x) for x in input().split()]
arr=[[]]*n
ans=[]
lastanswer=0
for _ in range(q) :
    z,x,y=[int(x) for x in input().split()]
    if z==1 :
        idx=((x^lastanswer)%n)
        arr[idx].append(y)
    else :
        idx=((x^lastanswer)%n)
        lastanswer=arr[idx][y%len(arr[idx])]
    print(arr)