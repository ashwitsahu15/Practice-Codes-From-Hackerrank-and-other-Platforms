# Increasing Substring



j=int(input())
for _ in range(j) :
    n=int(input())
    s=input()
    l=[]
    count=1
    for i in range(n) :
        try :
            if s[i]<s[i+1] :
                l.append(count)
                count+=1
            else :
                l.append(count)
                count=1
        except IndexError :
            l.append(count)
            count=1
    print("Case #"+str(_+1)+":",' '.join(str(x) for x in l))



# Longest Progression



cost=1
def out():
    global cost
    s="Case #"+str(cost)+":"
    return s
    cost+=1
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    
    if n<=3:
        print(out(),n)
        continue
    l=[2 for i in range(n)]
    r=[2 for i in range(n)]
    l[0]=1
    l[1]=2
    r[-1]=1
    r[-2]=2
    for i in range(1,n-1):
        if a[i]-a[i-1]==a[i+1]-a[i]:
            l[i+1]=l[i]+1
    for i in range(n-2,0,-1):
        if a[i]-a[i-1]==a[i+1]-a[i]:
            r[i-1]=r[i]+1
    maxx=max(l[-1],r[0],l[-2]+1,r[1]+1)
    for i in range(1,n-1):
        if i==1:
            if a[i+1]-a[i-1]==2*(a[i+2]-a[i+1]):
                maxx=max(maxx,r[2]+2)
            else:
                maxx=max(maxx,r[2]+1)
        elif i==n-2:
            if a[i+1]-a[i-1]==2*(a[i-1]-a[i-2]):
                maxx=max(maxx,l[n-3]+2)
            else:
                maxx=max(maxx,l[n-3]+1)
        else:
            if a[i+1]-a[i-1]==2*(a[i+2]-a[i+1]):
                maxx=max(maxx,r[i+1]+2)
            if a[i+1]-a[i-1]==2*(a[i-1]-a[i-2]):
                maxx=max(maxx,l[i-1]+2)
            maxx=max(maxx,r[i+1]+1)
            maxx=max(maxx,l[i-1]+1)
            if a[i+1]-a[i-1]==2*(a[i+2]-a[i+1]) and a[i+1]-a[i-1]==2*(a[i-1]-a[i-2]):
                maxx=max(maxx,r[i+1]+l[i-1]+1)
    print(maxx)