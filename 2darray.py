import sys

arr = []
for i in range(6):
    arr.append([int(j) for j in input().split()])
maxi = None
for a in range(4):
    for b in range(4):
        value = arr[a][b] + arr[a][b+1] + arr[a][b+2] + arr[a+1][b+1] + arr[a+2][b] + arr[a+2][b+1] + arr[a+2][b+2]
        if maxi == None or value > maxi:
            maxi = value
print(maxi)
