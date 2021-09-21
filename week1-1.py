def SieveOfEratosthenes(n): 
    l=[]
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):  
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]:
            l.append(p)
    return l       

 
for T in range(int(input())) :
    n=int(input())
    a=SieveOfEratosthenes(n)
    flag=0
    for i in range(len(a)) :
        for j in range(i+1,len(a)) :
            if a[i]*a[j]<=n :
                flag+=1
    print(flag)