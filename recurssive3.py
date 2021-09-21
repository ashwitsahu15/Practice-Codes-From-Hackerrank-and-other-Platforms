n=int(input())

def factorial(n) :
    ans=1
    while n-1>0  :
        ans=ans*n
        n-=1
    print(ans)
factorial(n)