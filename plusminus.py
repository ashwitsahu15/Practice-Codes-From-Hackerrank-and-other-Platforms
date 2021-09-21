n=int(input())
pos=0
neg=0
zero=0
arr=[int(i) for i in input().split()]
for _ in range(n) :
    if arr[_]>0 :
        pos+=1
    elif arr[_]<0:
        neg+=1
    else :
        zero+=1
print(pos/n)
print(neg/n)
print(zero/n)