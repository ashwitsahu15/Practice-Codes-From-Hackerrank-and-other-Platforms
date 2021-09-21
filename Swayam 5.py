import time
start_time = time.time()
for _ in range(int(input())) :
    s=input()
    s=list(s)
    count=0
    n=len(s)
    for i in range(n) :
        if s[i]=='1' :
            count+=1
            if i!=0 :
                if s[i-1]=='0' :
                    s[i-1]='2'
                    continue
            if i!=(n-1) :
                if s[i+1]=='0' :
                    s[i+1]='2'

    cnt=s.count('0')

    if cnt==count :
        print('-1')
    elif count>cnt :
        print('1')
    else :
        print('0')
print('--- %s seconds ---' % (time.time() - start_time))
