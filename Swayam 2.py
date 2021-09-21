import time
import math
start_time = time.time()
import math

def primecheck(n) :
    prime_flag = 0
    if(n > 1):
        for i in range(2,int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def countDivisors(n) :
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                cnt = cnt + 1
            else :
                cnt = cnt + 2
    return cnt

for _ in range(int(input())) :  
    count=0
    n=int(input())
    for i in range(1,n+1) :
        if primecheck(i)==False :
            if primecheck(countDivisors(i))==True :
                count+=1
    print(count)
print('--- %s seconds ---' % (time.time() - start_time))
