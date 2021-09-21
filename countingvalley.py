n=int(input())
s=input()
valley=0
ans=0
for i in s:
    if i=='U' :
        a=-1
    if i=='D' :
        a=1
    temp=a
    ans=a+ans
    if temp==-1 and ans==0 :
        valley+=1
print(valley)