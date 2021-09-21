n=[int(_) for _ in input().split()]
n.sort()
l=len(n)
mini=0
maxi=0
for _ in range(len(n)) :
    if _!=0 :
        maxi=n[_]+maxi
for _ in range(len(n)) :
    if _!=l-1 :
        mini=n[_]+mini
print(mini,maxi)