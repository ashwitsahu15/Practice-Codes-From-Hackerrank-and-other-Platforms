import time
start_time = time.time()
for _ in range(int(input())) :
    n=int(input())
    arr=[int(s) for s in input().split()]
    a=[]
    b=[]
    ans=[]
    for i in range(n) :
        if i%2==0 :
            a.append(arr[i])
        else :
            b.append(arr[i])
    a.sort()
    b.sort()
    cnt=0
    for i in range(n) :
        if i%2==0 :
            ans.append(a.pop(0))
        else :
            ans.append(b.pop(0))
    flag=0
    for i in range(n-1) :
        if ans[i]>ans[i+1] :
            flag=1
            value=i
            break
    if flag==1 :
        print("Case #"+str(_+1)+": "+str(i))
    else :
        print("Case #"+str(_+1)+": "+"OK")
print('--- %s seconds ---' % (time.time() - start_time))