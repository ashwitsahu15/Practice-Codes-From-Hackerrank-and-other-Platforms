# ans=0
# n=int(input())
# a=[int(s) for s in input().split()]
# m=int(input())
# b=[int(s) for s in input().split()]
# for i in range(n) :
#     if a[i]==0 :
#         l=(b[i]-b[i-1])
#         r=(b[i+1]-b[i])
#         mini=min(l,r)
#         ans+=mini    
# print(ans)





# s=input()
# print(s.count('a')


# a=input()
# a=list(a)
# n=int(input())
# for i in range(len(a)-n) :
#     (a[i],a[i+n-1])=(a[i+n-1],a[i])
# print(''.join(a))


# n=int(input())
# arr=[int(x) for x in input().split()]
# val=[int(x) for x in input().split()]
# count=0
# for i in arr :
#     val=[x%i for x in arr]
#     print(val)
#     if val.count(0)==len(val) :
#         count+=1
# print(count)

n=int(input())
arr=[int(x) for x in input().split()]
size=int(input())

ans=[]
for i in range(n-1) :
    sub=arr[i:i+size]
    for j in sub :
        if j<0 :
            ans.append(j)
            break
        else :
            ans.append(0)
ans=list(dict.fromkeys(ans))
print(*ans)