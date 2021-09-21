import sys
n=int(input())
d={}
for _ in range(n) :
    keys,values=input().split()
    d[keys]=values
lines = sys.stdin.readlines()  # convert lines to list
for i in lines:
    s = i.strip()
    if s in d:
        print(s + '=' + str(d[s]))
    else:
        print('Not found')