# l1=[int(x) for x in input().split()]
# length=len(l1)
# i=0
# maxi=0
# while(i<=length-1) :
#     j=i+1
#     while(j<=length) :
#         temp=(sum(l1[i:j])*min(l1[i:j]))
#         maxi=max(temp,maxi)
#         j+=1
#     i+=1
# print(maxi)


# def sublist(l1,l2):
#     l3=[]
#     n=len(l2)
#     l3=[l2[i:j+1] for i in range(n) for j in range(i,n)]
#     if l1 in l3 or l1==[]:
#         return True
#     else:
#         return False
# print(sublist([2,2,4],[2,2,3,4,5]))
# print(sublist([2,2,3],[2,2,3,4,5]))


n=1
while(input()!=" ") :
  n+=1
  if n%3==0 :
    print(input())