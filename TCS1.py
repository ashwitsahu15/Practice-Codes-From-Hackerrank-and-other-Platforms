# import math

# n=int(input())
# cars=[int(x) for x in input().split()]
# permutation=math.factorial(n)
# print(permutation)





# n=int(input())
# s=input()
# arr=[]
# for i in range(len(s)) :
#     if i%2!=0 :
#         arr.append(int(s[i]))
# s=input()
# arr2=[]
# for i in range(len(s)) :
#     if i%2!=0 :
#         arr2.append(int(s[i]))
# ans=[0]*n
# maxi=0
# for i in range(n) :
#     ans[i]=(arr[i]+ans[i-1])-arr2[i]
#     maxi=max(ans[i],maxi)
# print(maxi)


n=int(input())
ans=0
count=0
for i in range(n) :
    a=int(input())
    if a==0 :
        count+=1
    else :
        ans+=count
print(ans)