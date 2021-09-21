s=input()
t=input()
a=len(s)
b=len(t)
if b>a :
    s,t=t,s
    a,b=b,a
d={}
for i in t :
    if i not in d :
        d[i]=1
    else :
        d[i]+=1
count=len(d)
j=0
while j<a :
    