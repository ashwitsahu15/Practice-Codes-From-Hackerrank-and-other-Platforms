# for _ in range(int(input())) :
#     n=int(input())
#     ans=((n-1)*(n))/2
#     print(int(ans))

# p,q=[int(x) for x in input().split()]
# arr = [1 for i in range(q)]
# for i in range(p-1):
#     for j in range(1,q):
#         arr[j]+=arr[j-1]
# print(arr[q-1])
 

def Numberofpaths(m,n) :
    if(m==1 or n==1) :
        return 1
    return Numberofpaths(m-1,n)+Numberofpaths(m,n-1)
p,q=[int(x) for x in input().split()]
print(Numberofpaths(p,q))