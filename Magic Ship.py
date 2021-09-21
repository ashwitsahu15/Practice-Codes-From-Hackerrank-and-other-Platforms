x1,y1=[int(x) for x in input().split()]
x2,y2=[int(x) for x in input().split()]
n=int(input())
s=input()

x,y=(0,0)
loc=[(0,0)]
for i in s :
    if i=='U' :
        y+=1
    
    elif i=='D' :
        y-=1
    
    elif i=='R' :
        x+=1
    
    elif i=='L' :
        x-=1
    loc.append((x,y))

L=0;R=10**15
flag=0
while L!=R :
    mid=(L+R)//2

    days,rem=divmod(mid,n)

    xd=abs(x2-(x1+(days*x)+loc[rem][0]))
    yd=abs(y2-(y1+(days*y)+loc[rem][1]))

    if (xd+yd)<=mid :
        R=mid
    else :
        L=mid+1

    if L==10**15 :
        print(-1)
        flag=1
if flag==0 :
    print(R)