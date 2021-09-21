import time
start_time = time.time()
for _ in range(int(input())) :
    s,k=input().split()
    s=list(s)
    n=len(s)
    k=int(k)
    count=0
    for i in range(n-k+1) :
        if s[i]=='-' :
            for j in range(i,i+k) :                                             
                if s[j]=='-' :
                    s[j]='+'
                elif s[j]=='+' :
                    s[j]='-'
            count+=1
    impossible= False
    for i in range(n-k+1,n) :
        if s[i]=='-' :
            impossible=True
            break
    if impossible :
        print("Case #"+str(_+1)+": "+"IMPOSSIBLE")
    else :
        print("Case #"+str(_+1)+": "+str(count))
print('--- %s seconds ---' % (time.time() - start_time))