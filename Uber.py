# def almostSubstring(t, s):
#     count=0
#     for T in range(len(t)-4) :
#         print(t[T],s[0],s[1],s[2])
#         if t[T]==s[0] and t[T+2]==s[1] and t[T+4]==s[2] :
#             count+=1
#     return count

# def bestRhombicArea(matrix, radius):
#     l1=len(matrix)
#     l2=len(matrix[0])
#     if radius == 1:
#         return [matrix[l1//2][l2//2]]
#     ans=[]
#     for i in range(l1-radius) :
#         for j in range(l2-radius) :
#             ans.append(matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+1][j+2]+matrix[i+2][j+1])
#     ans=list(set(ans))
#     ans.sort(reverse=True)
#     return (ans[0:3])
# bestRhombicArea([[1, 1, 2, 3, 1],[2, 5, 2, 1, 7],[1, 4, 3, 1, 5],[6, 1, 4, 2, 0]],2)


def name(a,b,queries) :
    count1=0
    count2=0
    ans=[]
    flat=0
    for q in queries :
        if len(q)==2 :
            for i in range(len(a)) :
                for j in range(len(b)) :
                    if a[i]+b[j]==q[1] :
                        count1+=1
        else :
            temp=q[1]
            a[temp]=q[2]
            flat=1
    ans.append(count1)
    if flat==0 :
        ans.append(count2)
    return ans
print(name([1000000000],[1000000000],[[1,2000000000],[0,0,1000000000],[0,0,0],[1,2000000000]]))
print(name([2, 0, 2],[1, 0, 1],[[1,0]]))
print(name([95, 100, 15, 91],[4, 14, 84],[[1,105],[1,175],[0,2,58],[1,62]]))
