for _ in range(int(input())) :
    n=int(input())
    arr=[int(x) for x in input().split()]
    print(arr[0]-(sum(arr)-arr[0]))

n=int(input())
arr=[]
for _ in range(n) :
    arr.append(int(input()))
k=int(input())
# flag=0
# count=0
# temp=0
# for j in range(n//3) :
#     for i in range(3) :
#         if arr[i]==k :
#             flag=1
#     if flag==1 :
#         count+=1
#     temp+=1
# if k in arr[(3*temp):] :
#     count+=1
# print(temp,count)
# if temp+1==count :
#     print(1)
# else :
#     print(0)
i=0
while n>=3 :
    if k in [arr[i],arr[i+1],arr[i+2]] :
        flag=1
    else :
        flag=0
        break
    i+=3
    n-=3
if flag==1 :
    if k not in arr[i:] :
        flag=0
print(flag)