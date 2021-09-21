for T in range(int(input())) :
        n=int(input())
        s=input()
        l=[]
        for i in range(n) :
            l.append(s[(0+i):(n+i)])
        print(l)