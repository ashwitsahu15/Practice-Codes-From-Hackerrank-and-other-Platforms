n=int(input())
arr=[int(i) for i in input().split()]
value=0
for i in arr :
    value=max(value,arr.count(i))
print(n-value)