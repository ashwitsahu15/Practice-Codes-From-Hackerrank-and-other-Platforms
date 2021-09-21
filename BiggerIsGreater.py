t=int(input())
alphabet=ascii("a")
for T in range(t) :
    s=[str(x) for x in input().split()]
    start=-1
    for i in range(0,len(s)-1) :
        if s[i]<s[i+1] :
            start=i
    if start==-1 :
        print('no answer')
        continue
    end=-1
    for j in range(start+1,len())