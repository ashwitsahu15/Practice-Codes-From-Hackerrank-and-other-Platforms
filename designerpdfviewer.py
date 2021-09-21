import string
alphabet=list(string.ascii_lowercase)
arr=[int(i) for i in input().split()]
s=input()
finalarr=[]
for _ in s :
    temp=alphabet.index(_)
    finalarr.append(arr[temp])
print(max(finalarr)*len(s))