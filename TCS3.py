# # from sys import stdin
# city=[[]]
# for i in range(9) :
#     city.extend(list(input()))
# virus=(0,0)
# print(city[1])

# n=int(input())
# k=int(input())
# ans=1
# for i in range(2,k+1) :
#     temp=0
#     for j in range(2,i) :
#         temp+=j
#         ans+=(n//temp)-1
#     ans+=(n//i)
# print(ans)

# n=int(input())
# k=int(input())
# arr=[[0]*(n+1)]*(k+1)
# for i in range(n+1):
#   arr[0][i]=0
#   arr[1][i]=1
# for i in range(k+1):
#   arr[i][0]=0
# for a in range(2,k+1):
#   for b in range(1,n+1):
#     if b<a:
#       arr[a][b]=arr[a-1][b]
#     elif b==a:
#       arr[a][b]=arr[a-1][b]+1
#     else:
#       arr[a][b]=arr[a-1][b]+arr[a][b-a]
# print(arr[k][n])


# def div(num) :
#     ans=0
#     while num>0 :
#         ans+=num%10
#         num=num//10
#     return ans

# n=int(input())
# r=int(input())
# ans=0
# ans=div(n)
# while r>1 :
#     ans=div(ans)
#     r-=1
# print(ans)

# arr=[x for x in input().split()]
# ans=len(arr[-1])
# print ans 

# n=int(input())
# arr=[int(x) for x in raw_input().split()]
# arr.sort()
# ans1=[]
# ans2=[]
# for i in range(n) :
#   if i%2==0 :
#     ans1.append(arr[i])
#   else :
#     ans2.append(arr[i])
# ans=ans1+ans2
# for i in range(len(ans)) :
#   print(ans[i],sep='')


# # import math 
# r=int(input())
# c=int(input())
# ans=0
# if r%2==0:
#   for i in range(r//2) :
#     ans+=c
#   print(ans)
# else :
#   for i in range(r//2) :
#     ans+=c
#   ans+=math.ceil(c/2)
#   print(ans)

s=input()
ans=0
counts = []
count = 1
for a, b in zip(s, s[1:]):
    if a==b:
        count += 1
    else:
        counts.append((a, count))
        count = 1
counts.append((s[-1],count))
for i in range(len(counts)) :
    if counts[i][1]%2==0 :
        ans+=counts[i][1]
print(ans)