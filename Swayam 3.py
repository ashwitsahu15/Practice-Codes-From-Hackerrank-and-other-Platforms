import time
start_time = time.time()
def solve(n,k,arr) :
    m=arr.index(min(arr))
    temp=arr[m]
    while k!=0 :
        if m<n :
            if arr[m]==temp :
                arr[m]=10e9+1
            m+=1
        k-=1
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
ans=[10e9+1]*n
count=0
while (ans!=arr):
    solve(n,k,arr)
    count+=1

print(count)
print('--- %s seconds ---' % (time.time() - start_time))


