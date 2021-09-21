# for n in range(int(input())) :
#     count=0
#     i=input()
#     for I in range(len(i)) :
#         J=I+1
#         while(J<len(i)) :
#             if(i[I]>i[J]) :
#                 count+=1
#             J+=1
#     if(count>0) :
#         print("YES")
#     else :
#         print("NO")

# for n in range(int(input())) :
#     count=0
#     i=input()
#     temp=i
#     i=sorted(i)
#     s=''.join(map(str,i))
#     if(temp==s):
#         print("NO")
#     else:
#         print("YES")


l=[]
final=[]
n=int(input())
for N in range(n) :
    l.append(input())
s=set(l)
x=(n*5)/100
for S in s :
    if((l.count(S))>=x) :
        final.append(S)
final.sort()
for y in final :
    print(y)