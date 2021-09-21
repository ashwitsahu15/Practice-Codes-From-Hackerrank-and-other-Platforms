n=int(input())
score=[int(i) for i in input().split()]
maxi=score[0]
mini=score[0]
highest=0
lowest=0
for i in score :
    if i>maxi :
        maxi=i
        highest+=1
    elif i<mini :
        mini=i
        lowest+=1
print(highest,lowest)