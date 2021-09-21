s=input()
h=s[0]+s[1]
h=int(h)
if s[8]=='P' :
    h=h+12
    if h==24:
        h='12'
        print(h+s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
    else :
        h=str(h)
        print(h+s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
elif s[8]=='A' :
    if h==12 :
        h='00'
        print(h+s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
    else :
        for _ in range(8) :
            print(s[_],end='')
    
