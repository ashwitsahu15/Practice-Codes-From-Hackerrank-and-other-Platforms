x1,v1,x2,v2=[int(i) for i in input().split()]
# if v2-v1==0 :
#     print('NO')
# else :
#     t=(x1-x2)/(v2-v1) 
#     if abs(int(t)-t)<0.05 and t>0 :
#         print('YES')
#     else :
#         print('NO')

if v2-v1==0 :
    print('NO')
elif x1<x2 and v2>v1 :
    print('NO') 
else :    
    x=((v2*x1)-(v1*x2))/(v2-v1)
    if x<0 :
        print('NO')
    else :
        if (x-x1)%v1==0 and (x-x2)%v2==0 :
            print('YES')
        else :
            print('NO')

 
