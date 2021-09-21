for j in range(int(input())) :
    n,k=[int(x) for x in input().split()]
    s=input()
    count=0
    i=0
    n=n-1
    while k!=0 or i<=n//2 :
        if (n-i+1)<n :
            if s[i] != s[n-i+1] :
                k-=1
            else :
                count+=1
                k-=1
            print(i,n-i+1,k,count)
        i+=1
    print("Case #"+str(j+1)+": "+str(count))