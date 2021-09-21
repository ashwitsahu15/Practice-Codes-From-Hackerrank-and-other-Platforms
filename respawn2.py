from sys import stdin 

for T in range(int(input())) :
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in stdin.readline().split()]
    total=sum(arr)
    if total%k==0 :
        print(int(total/k))
    else :
        print(int((total/k))+(total%k))    