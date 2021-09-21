def Isprime(n) :
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True


for t in range(int(input())) :
    n=int(input())
    f=[int(x) for x in input().split()]
    ans=[]
    i=0
    l=len(f)
    while (i<l) :
        print(i,f[i])
        if Isprime(f[i])==True :
            ans.append(i+1)
        
        i+=1
    print(ans)

l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
temp=l1
for i in range(len(l1)) :
    if i%2!=0 :
        temp=l1[i]
        l1[i]=l2[i]
        l2[i]=temp
print(l1,l2)
