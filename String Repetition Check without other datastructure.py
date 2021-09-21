def chkstr(n) :
    flag=True
    a=[]
    for i in n :
        if i not in a :
            a.append(i)
        else :
            flag=False 
            break
    return flag

# USING STL
def string(n) :
    n=list(n)
    n.sort()
    for i in range(len(n)-1) :
        if n[i]==n[i+1] :
            return False
    return True
print(string("aba"))
