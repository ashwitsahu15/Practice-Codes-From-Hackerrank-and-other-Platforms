def merge(a,b) :
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while (i+j)<(m+n) :
        if i==m :
            c.append(b[j])
            j+=1
        elif j==n :
            c.append(a[i])
            i+=1
        elif a[i]<=b[j] :
            c.append(a[i])
            i+=1
        elif a[i]>b[j] :
            c.append(b[j])
            j+=1
    return(c)

def mergesort(a,left,right) :
    if right-left<=1 :
        return(a[left:right])
    
    if right-left>1 :
        mid=(right+left)//2
        l=mergesort(a,left,mid)
        r=mergesort(a,mid,right)
        return merge(l,r)

a=list(range(0,100,2)) + list(range(1,100,2))

print(mergesort(a,0,len(a)))