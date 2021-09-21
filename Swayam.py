import time
import math
start_time = time.time()
for _ in range(int(input())) :
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    L=0
    R=1.1*(10**12)
    temp=n
    for i in range(n) :
        L=math.ceil(max(L,(a[i]*k)/(i+1)))
        R=math.ceil(min(R,((a[i]+1)*k)/(i+1)))
        print(L,R-1)
     
print('--- %s seconds ---' % (time.time() - start_time))