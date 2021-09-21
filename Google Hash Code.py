import sys

sys.stdout=open('f_ans.txt','w')
sys.stdin=open('f.txt','r')

(total_time,intersections,streets,cars,bonus)=[int(x) for x in input().split()]
desc_of_streets=[]
end_points=[]
maxi=0

for _ in range(streets) :
    (start_point,end_point,street_name,time_taken)=[y for y in input().split()]
    desc_of_streets.append((start_point,end_point,street_name,time_taken))
    end_points.append(int(end_point))
mini=int(time_taken)
d = {}
for each in desc_of_streets:
    maximum=max(mini,int(each[3]))
    mini=min(mini,int(each[3]))
    x=(maximum+mini)//2
    if each[1] not in d.keys():
        d[each[1]] = [(each[2],x)]
    else:
        d[each[1]].append((each[2],x))

path=[]
for car in range(cars) :
    path.append(input().split())
    maxi=max(int(path[car][0]),maxi)
print(maxi)
for m in range(maxi) :
    print(m)
    print(end_points.count(m))
    for each in d[str(m)] :
        print(*(list(each)))