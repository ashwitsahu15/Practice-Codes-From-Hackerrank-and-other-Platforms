from sys import stdin

n=int(input())
mini=n
a=[int(x) for x in input().split()]
print(list(set(a)))
print(a)
if sorted(list(set(a)))==sorted(a) :
    print(-1)
else :
    for i in range(len(a)) :
        j=0
        while j<n :
            if a[i]==a[j] and i!=j :
                mini=min(mini,abs(j-i))
            j+=1
    print(mini)