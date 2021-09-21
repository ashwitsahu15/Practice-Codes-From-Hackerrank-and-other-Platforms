n=int(input())
color=[int(i) for i in input().split()]
pair=0
identical=set(color)
identical=list(identical)
for _ in identical :
    value=color.count(_)
    indivisualpair=value//2
    pair+=indivisualpair
print(pair)