n=int(input())
arr=[]
for i in range(n) :
    num=int(input())
    arr.append(num)
temp=set(arr)
temp=list(temp)
for _ in range(len(temp-1)) :
    if temp[_+1]-temp[_]==1 :
        subarray.append([temp[_+1] for temp[_+1] in arr if temp[_+1] == '' and (_+a) <= t])