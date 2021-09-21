# n=int(input())
# ans=0
# i=1
# while i<n+1 and i%2!=0 :
#     ans+=(((-1)**i)*i)
#     if i<n :
#         ans+=(i+1)
#     i+=2
# print(ans)



# n=int(input())
# ans=0
# a=n//2
# ans+=(a**2)+(a)
# if n%2==0 :
#     # ans-=(a/2)*(1+(n-1))
#     ans-=(a)**2
# else :
#     # ans-=((a+1)/2)*(1+n)
#     ans-=((a+1)**2)
# print(int(ans))



def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
        for alpha in range(n**2) :
            for i in range(l, n):
                a[k][i]=alpha
            k += 1
            for i in range(k, m):
                a[i][n - 1]=alpha
            n -= 1
            if (k < m):
    
                for i in range(n - 1, (l - 1), -1):
                    a[m - 1][i]=alpha
                m -= 1
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    a[i][l]=alpha
    
                l += 1
n=int(input())
a=[]
spiralPrint(n,n,a)
print(a)