def digittoword(x) :
    if x==1 :
        return 'one'
    elif x==2 :
        return 'two'
    elif x==3 :
        return 'three'
    elif x==4 :
        return 'four'
    elif x==5 :
        return 'five'
    elif x==6 :
        return 'six'
    elif x==7 :
        return 'seven'
    elif x==8 :
        return 'eight'
    elif x==9 :
        return 'nine'
    elif x==10 :
        return 'ten'
    elif x==11 :
        return 'eleven'
    elif x==12 :
        return 'twelve'
    elif x==13 :
        return 'thirteen'
    elif x==14 :
        return 'fourteen'
    elif x==15 :
        return 'fifteen'
    elif x==16 :
        return 'sixteen'
    elif x==17 :
        return 'seventeen'
    elif x==18 :
        return 'eighteen'
    elif x==19 :
        return 'nineteen'
    elif x==20 :
        return 'twenty'
    elif x==21 :
        return 'twenty one'
    elif x==22 :
        return 'twenty two'
    elif x==23 :
        return 'twenty three'
    elif x==24 :
        return 'twenty four'
    elif x==25 :
        return 'twenty five'
    elif x==26 :
        return 'twenty six'
    elif x==27 :
        return 'twenty seven'
    elif x==28 :
        return 'twenty eight'
    elif x==29 :
        return 'twenty nine'

a=int(input())
b=input()
temp=b
b=int(temp[0])
if len(temp)==2 :
    c=int(temp[1])
else :
    c=b
    b=0
if b==0 and c==0 :
    print(digittoword(a)+" o' clock")
elif b==1 and c==5 :
    print("quarter past "+digittoword(a))
elif b==3 and c==0 :
    print("half past "+digittoword(a))
elif b==4 and c==5 :
    print("quarter to "+digittoword(a+1))
elif b==0 and c==1 :
    print(digittoword(int(temp))+" minute past "+digittoword(a))
elif b<3 :
    print(digittoword(int(temp))+" minutes past "+digittoword(a))
elif b>=3 :
    print(digittoword(60-int(temp))+" minutes to "+digittoword(a+1))