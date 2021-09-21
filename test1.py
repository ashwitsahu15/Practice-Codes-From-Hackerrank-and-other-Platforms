t=int(input())
for T in range(t) :
    ans=[len(s) for s in input().split('0') if len(s)>0]
    ans.sort(reverse=True) 
    print(sum(ans[0::2]))