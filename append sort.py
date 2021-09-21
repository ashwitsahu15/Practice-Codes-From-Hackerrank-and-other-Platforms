# for _ in range(int(input())) :
#     ans=0
#     n=int(input())
#     l=[int(x) for x in input().split()]
#     for i in range(len(l)-1) :
#         count=0
#         while l[i+1]<=l[i] :
#             l[i]=str(l[i])
#             l[i+1]=str(l[i+1])
#             temp=l[i+1]
#             l[i+1]=l[i+1]+'9'*(len(l[i])-len(l[i+1])+count)
#             ans=ans+len(l[i+1])-len(temp)
#             # print(l[i+1],l[i],ans)
#             l[i]=int(l[i])
#             l[i+1]=int(l[i+1])
#             count+=1
#     print("Case #"+str(_+1)+": "+str(ans))

def modified(a, b):
    thisCount = 0
    # no change
    if b > a:
        return b,thisCount

    working = b

    lendiff = len(str(a)) - len(str(b))
    working = int(str(b) + "0"*lendiff)
    thisCount += lendiff

    if working > a:
        return working, thisCount

    # calculate offset
    offset = a - working
    if (offset >= (10**lendiff - 1)):
        working = int(str(working) + "0")
        thisCount += 1
    else:
        working += offset + 1

    return working, thisCount

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0

    for i in range(1, n):
        nums[i], thisCount = modified(nums[i-1], nums[i])
        count += thisCount

    print("Case #{}: {}".format(test_case, count))