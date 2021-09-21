# n=int(input())
# count=0
# a=[int(x) for x in input().split()]
# for i in range(n-1) :
#     for j in range(0,n-i-1) :
#         if a[j]>a[j+1] :
#             a[j],a[j+1]=a[j+1],a[j]
#             count+=1
# print("Array is sorted in",count,"swaps.")
# print("First Element:",a[0])
# print("Last Element:",a[n-1])

l=[]
maxi=0
for x in range(6) :
    l.append([int(x) for x in input().split()])
for i in range(4) :
    for j in range(4) :
        value=l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j+1]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2]
        if value>maxi :
            maxi=value

print(maxi)