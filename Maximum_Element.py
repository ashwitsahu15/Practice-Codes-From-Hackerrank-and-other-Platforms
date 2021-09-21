n=int(input())
st=[]
for _ in range(n) :
    op=input()
    if op=='2' :
        st.pop()    
    elif op=='3' :
        print(st[-1])
    else :
        op=int(op[2:])
        if len(st)==0 :
            st.append(op)
        else :
            maxi=st[-1]
            st.append(op if op>maxi else maxi)
