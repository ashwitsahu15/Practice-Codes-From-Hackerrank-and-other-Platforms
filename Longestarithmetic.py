# from sys import stdin,maxsize
# import operator

# t=int(input())
# for T in range(t) :
#     n=int(input())
#     maxi=0
#     i=0
#     a=[int(x) for x in stdin.readline().split()]
#     a=list(map(operator.sub, a[1:], a[:-1]))
#     flag=1
#     while i<(n-2) :
#         if a[i]==a[i+1]:
#             flag+=1
#         else :
#             flag=1
#         maxi=max(maxi,flag)
#         i+=1
#     print('case #'+str(T+1)+": "+str(maxi+1))



from sys import stdin

t=int(input())
for T in range(t) :
    n=int(input())
    a=[int(x) for x in stdin.readline().split()]
    b=[0]*(n-1)
    for i in range(n-1) :
        b[i]=a[i+1]-a[i]
    i=0
    maxi=0
    flag=1
    while i<n-2 :
        if b[i]==b[i+1]:
            flag+=1
        else :
            flag=1
        maxi=max(maxi,flag)
        i+=1
    print('Case #'+str(T+1)+": "+str(maxi+1))