n=int(input())
a=[int(i) for i in input().split()]
s=set(a)
s=list(s)
s.sort()
maxi=0
if len(s)==1 :
    print(len(a))
else :
    for i in range(0,len(s)-1) :
        for j in range(1,len(s)) :
            if abs(s[j]-s[i])<=1 :
                ans=[]
                for _ in a :
                    if _==s[i] or _==s[j] :
                        ans.append(_)
                maxi=max(len(ans),maxi)
    print(maxi)