d1,m1,y1=[int(i) for i in input().split()]
d2,m2,y2=[int(i) for i in input().split()]
if y1>y2 :
    print(10000)
elif m1>m2 and y1==y2:
    print(500*(m1-m2))
elif d1>d2 and m1==m2 and y1==y2:
    print(15*(d1-d2))
else :
    print(0)