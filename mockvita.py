# n = int(input())
# b = input()
# b = list(b)
# g = input()
# g = list(g)
# p = 0

# for i in range(0,n) :
#     for j in range(0,n) :
#         if b[i] == g[j] :
#             del b[i]
#             del g[j]
#             k = 1
#         else :
#             k = 0
#     if k == 1 :
#         p = p
#     else :
#         p += 1

# print(p)

n=int(input())
b=input()
g=input()
len1=len(b)
len2=len(g)
k=0
a=0
for i in range(len1) :
    for j in range(len2) :
        if b[i]==g[j] :
            b = ''.join([b[x] for x in range(len(b)) if x != i])
            g = ''.join([g[y] for y in range(len(g)) if y != j])
            len1=len1-1
            len2=len2-1
            i=0
            j=0
            print(b,g,len1,len2,i,j)
            k=k
            continue
        else :
            k+=1
    if k==k :
        a=a
    else :
        a+=1
print(a)
    
















