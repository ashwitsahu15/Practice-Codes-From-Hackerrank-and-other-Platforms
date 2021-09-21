import time
import math
start_time = time.time()
for _ in range(int(input())) :
    n,m=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    arr.sort()
    L,R=1,arr[n-1]
    ans=10e9
    while L<R :
        mid=int((L+R)/2)
        ans=sum([math.ceil(x/mid) for x in arr])
        if ans<=m :
            R=int(mid)
        else :
            L=int(mid)+1
    print(math.ceil(L))
print('--- %s seconds ---' % (time.time() - start_time))