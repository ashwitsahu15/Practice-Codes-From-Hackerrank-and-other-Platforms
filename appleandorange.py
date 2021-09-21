s,t=[int(i) for i in input().split()]
a,b=[int(i) for i in input().split()]
m,n=[int(i) for i in input().split()]
#ad stands for apple's Distance
ad=[int(j) for j in (input().split())]
#od stands for orange's Distance
od=[int(j) for j in (input().split())]
apple=sum([1 for _ in ad if (_+a) >= s and (_+a) <= t])
orange=sum([1 for _ in od if (_+b) >= s and (_+b) <= t])
print(apple)
print(orange)


# s,t = map(int, input().strip().split(' '))
# a,b = map(int, input().strip().split(' '))
# m,n = map(int, input().strip().split(' '))
# apple = list(map(int, input().strip().split(' ')))
# orange = list(map(int, input().strip().split(' ')))

# sapple = sum([1 for f in apple if (f+a) >= s and (f+a) <= t])
# sorange = sum([1 for f in orange if (f+b) >= s and (f+b) <= t])

# print (sapple)
# print (sorange)