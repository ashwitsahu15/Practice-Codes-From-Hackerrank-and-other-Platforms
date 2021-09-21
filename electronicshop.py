b,n,m=[int(i) for i in input().split()]
keyboard=[int(i) for i in input().split()]
drives=[int(i) for i in input().split()]
i=0
maxi=0
while i<len(keyboard) :
    for j in drives :
        if (keyboard[i]+j)>maxi and (keyboard[i]+j)<=b :
            maxi=(keyboard[i]+j)
    i+=1
if maxi==0 :
    print('-1')
else :
    print(maxi)
