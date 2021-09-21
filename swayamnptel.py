# def contracting(l) :
#     ans=True
#     res = [l[i + 1] - l[i] for i in range(len(l)-1)]
#     print(res)
#     for i in range(len(res)-1) :
#         if res[i]<res[i+1] :
#             ans=False
#             break
#     return ans
# print(contracting([9,2,7,3,1]))
# print(contracting([-2,3,7,2,-1]))
# print(contracting([10,7,4,1]))


def contracting(l):
    final=[]
    f=abs(int(l[0]))+abs(int(l[1])+100)
    for p in range(len(l)-1):
        diff=abs(int(l[p])-int(l[p+1]))
#print(&quot;diff=&quot;,diff,f)
        if diff<f:
            final.append(diff)
            f=diff
        else:
            break
    return(len(final)==(len(l)-1))

def leftrotate(m):
    q=[]
    for i in range(len(m)):
        s=[]
        for j in range(len(m[i])):
#print(p[j][len(p)-1-i])
            s.append(m[j][len(m)-1-i])
        q.append(s)
    return(q)

def counthv(l):
    new_list=[]
    hc=[]
    vc=[]
    for k in l:
        new_list.append(int(k))
    for a in range(1,len(new_list)-1):
        if new_list[a]>new_list[a+1] and new_list[a]>new_list[a-1]:
            hc.append(new_list[a])
        if new_list[a]<new_list[a+1] and new_list[a]<new_list[a-1]:
            vc.append(new_list[a])
    return([len(hc),len(vc)])



print(contracting([9,2,7,3,1]))
print(contracting([-2,3,7,2,-1])) 
print(contracting([10,7,4,1]))
print(counthv([1,2,1,2,3,2,1]))
print(counthv([1,2,3,1]))
print(counthv([3,1,2,3]))
print(leftrotate([[1,2],[3,4]]))
print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))
print(leftrotate([[1,1,1],[2,2,2],[3,3,3]]))