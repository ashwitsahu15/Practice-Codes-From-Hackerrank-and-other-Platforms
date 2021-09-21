# n,m=[int(i) for i in input().split()]
# person=[]
# value=0
# ways=[]
# for i in range(n) :
#     person.append(input())
# i=0
# while i<n-1 :
#     for j in range(1,n) :
#         if i!=j and j>i:
#             ans=[0]*m
#             for k in range(m) :
#                 if person[i][k]=='1' or person[j][k]=='1' :
#                     ans[k]=1
#             ways.append(ans.count(1))
#         value=max(value,ans.count(1))
#     i+=1
# print(value)
# print(ways.count(value))

# n,m=[int(N) for N in input().split()]
# topics=[]
# for N in range(n) :
#     topics.append(input())
# print(topics)
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
persons = []
for _ in range(n):
   person = str(input().strip())
   persons.append(person)
print(persons)

size = len(persons)
max_topics_numbers = 0
teams = 0
for i in range(0, size):
    for j in range(i + 1, size):
        topics = str("{0:b}".format((int(persons[i], 2) | int(persons[j], 2))))
        print(persons[i],persons[j],topics)
        