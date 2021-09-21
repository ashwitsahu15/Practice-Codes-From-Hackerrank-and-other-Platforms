s=input()
rep=[-1]
count=0
for i in s :
    if i not in rep :
        count+=1
        rep.append(i)
    else :
        break
    
print(count)