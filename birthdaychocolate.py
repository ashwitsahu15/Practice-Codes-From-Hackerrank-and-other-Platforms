n=int(input())
s=[int(i) for i in input().split()]
d,m=[int(i) for i in input().split()]
temp=0
flag=0
while m<=len(s) :
    pair=[]
    for j in range(temp,m) :
        pair.append(s[j])
    if sum(pair)==d :
        flag+=1
    temp+=1
    m+=1
print(flag)
