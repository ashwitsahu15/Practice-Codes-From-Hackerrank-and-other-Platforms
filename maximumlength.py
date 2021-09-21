from sys import stdin


# def lenOfLongIncSubArr(arr, n) : 
#     m = 1
#     l = 1 
#     for i in range(1, n) : 
#         if (arr[i] > arr[i-1]) : 
#             l =l + 1 
#         else : 
#             if (m < l)  : 
#                 m = l    
#             l = 1
#     if (m < l) : 
#         m = l

#     return m 


n=int(input())
ans=1
maxi=0
arr=[int(x) for x in stdin.readline().split()]
for i in range(len(arr)-1) :
    if arr[i+1]>arr[i] :
        ans+=1
    else :
        maxi=max(maxi,ans)
        ans=1
maxi=max(maxi,ans)
print(maxi)