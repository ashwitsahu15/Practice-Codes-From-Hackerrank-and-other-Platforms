n=int(input())
i=1
j=n-1
while i<n+1 :
    while j>=0 :
        space=' '*j
        ans='#'*i
        print(space+ans)
        j-=1
        i+=1
        break
    