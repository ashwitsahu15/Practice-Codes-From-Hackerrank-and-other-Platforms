# TIME COMPLEXITY CHECK


def countX(lst, x): 
    return lst.count(x)

n=int(input())
customer=[]
final=[]
for _ in range(n) :
    s=input()
    customer.append(s)
temp=set(customer)
temp=list(temp)
for _ in temp :
    ans=countX(customer,_)
    ans=(ans/n)*100
    if ans >= 5 :
        final.append(_)
final.sort()
for _ in final :
    print(_)
