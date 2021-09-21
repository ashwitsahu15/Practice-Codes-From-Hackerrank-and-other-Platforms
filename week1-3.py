# from sympy import *
# print(isprime(2))

# for _ in range(int(input())) :
#     n=int(input())
#     if n==1 :
#         print("Yes")
#     elif (n>=10 and(n%10==0)) :
#         print("Yes")
#     else :
#         print("No")

# n=int(input())
# ans=[int(i) for i in range(1,n) if n%i==0]
# print(ans)




# To BE READ

def spiral(m,n,a):
    i=0
    j=0
 
    while i<n and j<m :
        # Left to Right 
        for z in range(n) :
            print(matrix[i][z])
        i+=1
        # Top to Bottom
        for z in range(i,m) :
            print(matrix[z][n-1])
        n-=1

        if i<n :
            # Right to Left
            for z in range(n-1,j-1,-1) :
                print(matrix[m-1][z])
            m-=1
            # Bottom to Top
            for z in range(m-1,i,-1) :
                print(matrix[z][j])
            j+=1

matrix=[]
m,n=[int(i) for i in input().split()]
for M in range(1,m+1) :
    a=[]
    for N in range(1,n+1) :
        a.append(int(input()))
    matrix.append(a)
print(matrix)
spiral(m, n, matrix)

# Lower Triangle value printing
        