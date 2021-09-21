y=int(input())
if y>=1700 and y<=1917 :
    if y%4==0 :
        # leap year
        print('12.09'+'.'+str(y))
    else :
        print('13.09'+'.'+str(y))
elif y==1918 :
    print('26.09.1918')
elif y>=1919 and y<=2700 :
    if y%400==0 or y%4==0 and y%100!=0 :
        # leap Year
        print('12.09'+'.'+str(y))
    else :
        print('13.09'+'.'+str(y))