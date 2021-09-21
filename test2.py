from sys import stdin

def sub_lists(list1): 

    flag=0
    for i in range(len(list1) + 1): 
        for j in range(i + 1, len(list1) + 1): 
            sub = list1[i:j]
            if len(sub)==sum(sub) :
                flag+=1
              
      
    return flag

t=int(input())
for T in range(t) :
    n=int(input())
    arr=[int(x) for x in input()]
    print(sub_lists(arr))