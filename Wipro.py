# import time
# start_time = time.time()

# s=input()
# ans=0
# for i in range(len(s)) :
#     if int(s[i])%2==0 :
#         ans+=int(s[i])
# print(ans)
# # print('--- %s seconds ---' % (time.time() - start_time))


# s=input()
# s=list(s)
# s=[int(x) for x in s]
# print(min(s))

n=int(input())
arr=[int(x) for x in input().split()]
count=0
for i in arr :
    if i<0 :
        count+=1
print(count)


# s=input()
# s=[int(x) for x in s]
# for i in range(len(s)-1) :
#     if i%2==0 :
#         (s[i],s[i+1])=(s[i+1],s[i])
# print(*s,sep='')