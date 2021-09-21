t=int(input())
for i in range(t) :
    flag=0
    n=int(input())
    number=[int(i) for i in str(n)]
    for j in range(len(number)) :
        if int(number[j])==0 :
            pass
        elif (n%int(number[j]))==0 :
            flag+=1
    print(flag)
