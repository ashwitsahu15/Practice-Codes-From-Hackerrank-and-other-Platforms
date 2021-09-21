from bisect import bisect_right
n=int(input())
scores=sorted(list(set([int(i) for i in input().split()])))
l=len(scores)
m=int(input())
alice=[int(i) for i in input().split()]
for i in alice :
    print(l-bisect_right(scores,i)+1)
#     scores.append(i)
#     scores=sorted(scores,reverse=True)
#     print(scores.index(i)+1)