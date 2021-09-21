n,m=[int(x) for x in input().split()]
a=[]

for i in range(m) :
    c,d=[int(x) for x in input().split()]
    a.append((c,d))
a=sorted(a,key=lambda x : x[1])
temp=0
count=0
for i in a :
    if i[0]<temp:
        continue
    else :
        temp=i[1]
        count+=1
print(count)