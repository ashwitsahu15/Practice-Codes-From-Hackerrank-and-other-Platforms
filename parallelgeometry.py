for T in range(int(input())) :
    arr=[int(x) for x in input().split()]
    final=[]
    s=list(set(arr))
    for i in s :
        final.append((arr.count(i))%4)
    if sum(final)==0 :
        print('yes')
    else :
        print('no')
