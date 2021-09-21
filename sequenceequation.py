n=int(input())
p=[int(i) for i in input().split()]
for x in range(1,n+1) :
    temp=p.index(x)+1
    temp2=p.index(temp)+1
    print(temp2)