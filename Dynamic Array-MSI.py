# n=int(input())
# s=input()
# temp=set(list(s))
# for i in temp:
#     print(i,"occurs",s.count(i),"times")


# n=int(input())
# s=bin(n).replace("0b","")
# if s.count("1")==0 :
#     print("Invalid Input")
# else :
#     print(s.count("1"))
def pali(n) :
    rev=0
    while(n > 0):
        a=n%10
        rev=rev*10+a
        n=n//10
    return rev

s=input()
hour=int(s[0]+s[1])
# h=hour
minute=int(s[-2]+s[-1])
# m=minute
ans=0
while(hour!=pali(minute)) :
    if minute==60 :
        hour+=1
        minute=00
    if hour==24 :
        hour=00
    minute+=1
    ans+=1
print(ans)
