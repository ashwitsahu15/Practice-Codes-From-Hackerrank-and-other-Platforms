n=int(input())
arr=[int(i) for i in input().split()]
while len(arr)!=0 :
    print(len(arr))
    arr=[(x-min(arr)) for x in arr]
    arr=[x for x in arr if x!=0]