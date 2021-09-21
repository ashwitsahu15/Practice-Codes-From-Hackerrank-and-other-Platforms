n,k,q=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
# a = (a[-k:] + a[:-k])
for i in range(q) :
    t=int(input())
    print(a[(t+n-k)%n])