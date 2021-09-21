alice=0
bob=0
a=[int(j) for j in input().split()]
b=[int(j) for j in input().split()]
for _ in range(3) :
    if a[_] > b[_] :
        alice=alice+1
    elif a[_] < b[_] :
        bob=bob+1
    else :
        pass

print(alice, end=' ')
print(bob)
