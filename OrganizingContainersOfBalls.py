q=int(input())
for _ in range(q) :
    n=int(input())
    row=[0]*n
    column=[0]*n
    for x in range(n) :
        M=[int(x) for x in input().split()]
        for y in range(n) :
            row[x]+=M[y]
            column[y]+=M[y]
    print("Possible" if sorted(row)==sorted(column) else "Impossible")