# n=int(input())
def isprime(n) :
    if n<=1 :
        return False 
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True
def prime(n) :
    flag1=0
    flag2=0    
    ans1=0
    ans2=0
    (a,b)=(n,n)
    while(flag1==0 or flag2==0) :
        a=a+1
        b=b-1
        if isprime(a) and flag1==0:
            ans1=a
            flag1=1
        if isprime(b) and flag2==0 :
            ans2=b
            flag2=1
    if (ans1-n)==(n-ans2) :
        return ans2,ans1
    elif (ans1-n)<(n-ans2) :
        return ans1
    else :
        return ans2
print(prime(30))