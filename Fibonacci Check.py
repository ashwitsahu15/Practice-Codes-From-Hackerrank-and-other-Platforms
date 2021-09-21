import math
n=int(input())
ans1=(5*(n**2))+4
ans2=(5*(n**2))-4
if math.ceil(math.sqrt(ans1))==math.floor(math.sqrt(ans1)) or math.ceil(math.sqrt(ans2))==math.floor(math.sqrt(ans2)) :
    print(n)
else :
    f=[0,1]
    for i in range(n-1) :
        if (f[i]+f[i+1])<n :
            f.append(f[i]+f[i+1])
        else :
            break
    ans=sum([x for x in f if x%2==0])
    print(ans)