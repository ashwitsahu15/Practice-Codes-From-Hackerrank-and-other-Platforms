n,k=[int(i) for i in input().split()]
r,c=[int(i) for i in input().split()]
obstacles=[]
rows=[]
columns=[]
ans=0
for i in range(k) :
    obstacles.append([int(j)-1 for j in input().split()])
    rows.append(obstacles[i][0])
    columns.append(obstacles[i][1])
    total=n+n-2
print(obstacles)
print(rows)
print(columns)