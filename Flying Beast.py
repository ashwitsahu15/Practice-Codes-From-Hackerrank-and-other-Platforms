for t in range(int(input())) :
    n=int(input())
    maxi=0
    mini=0
    for i in range(1,n+1) :
        maxi=maxi+(i*i)
        mini=mini+(i*(n+1-i))
    print(maxi-mini)