n,k=[int(i) for i in input().split()]
bill=[int(i) for i in input().split()]
b=int(input())
bill.pop(k)
# value is b Actual
value=(sum(bill))/2 
if b==value :
    print('Bon Appetit')
elif b>value :
    print(int(b-value))