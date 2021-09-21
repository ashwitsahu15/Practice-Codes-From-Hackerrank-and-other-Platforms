def reverse_int(num) :
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev*10) + rem
        num = num//10
    return "%d " %rev

i,j,k=[int(x) for x in input().split()]
flag=0
for x in range(i,j+1) :
    if abs(x-int(reverse_int(x)))%k==0 :
        flag+=1
print(flag)