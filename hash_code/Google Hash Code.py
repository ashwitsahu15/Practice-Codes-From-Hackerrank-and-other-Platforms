import sys

sys.stdout=open('a_ans.txt','w')
sys.stdin=open('a.txt','r')

(total_time,intersections,streets,cars,bonus)=[int(x) for x in input().split()]
desc_of_streets=[]
end_points=[]
maxi=0
for _ in range(streets) :
    (start_point,end_point,street_name,time_taken)=[y for y in input().split()]
    desc_of_streets.append((start_point,end_point,street_name,time_taken))
    end_points.append(int(end_point))
d = {}
for each in desc_of_streets:
    if each[1] not in d.keys():
        d[each[1]] = [(each[2],int(each[3]))]
    else:
        d[each[1]].append((each[2],int(each[3])))

path=[]
for car in range(cars) :
    path.append(input().split())
    maxi=max(int(path[car][0]),maxi)
print(maxi-1)
for m in range(maxi-1) :
    print(m)
    print(end_points.count(m))
    for each in d[str(m)] :
        print(*(list(each)))