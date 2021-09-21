n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
s=[]
for M in range(m) :
    s=list(input())
    for i in range(len(s)) :
        if s[i]=='?' :
            s[i]='0'
    s=''.join(s)
    