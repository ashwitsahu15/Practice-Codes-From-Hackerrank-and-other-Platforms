for t in range(int(input())) :
    s=input()
    length=len(s)
    seg1=0
    seg2=0
    if s[0]=='Y' :
        seg1+=1
    else :
        seg2+=1
    for j in range(length-1) :
        if s[j]=='X' :
            if s[j+1]=='Y' :
                seg1+=1
        else :
            if s[j+1]=='X' :
                seg2+=1
    print(min(seg1,seg2))