n=int(input())
temp=n-1
arr = []
# rd=right diagonal
rd=0
# ld=left diagonal
ld=0
for i in range(n):
    arr.append([int(j) for j in input().split()])
for i in range(n) :
    for j in range(n) :
        if i==j :
            rd=arr[i][j]+rd
for i in range(n) :
    for j in range(n) :
        if i+j==temp :
            ld=arr[i][j]+ld
ans=rd-ld
if ans>0 :
    print(ans)
elif ans<0 :
    ans=ans*(-1)
    print(ans)
else :
    print(ans)        