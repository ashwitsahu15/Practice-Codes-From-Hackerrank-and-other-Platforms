nums=[int(x) for x in input().split()]
target=int(input())
temp=nums
# nums.sort()
count=0
ans=[]
for i in range(len(temp)) :
    for j in range(i+1,len(temp)) :
        if temp[i]<=target and temp[j]<=target :
            if temp[i]+temp[j]==target :
                print(i,j)
                ans.append(i)
                ans.append(j)
                count+=1
        if count==1 :
            break
    if count==1 :
        break
# print(nums)
print(ans)