def nextmultiple(num) :
    return ((5*int(num/5))+5)

n=int(input())
grades=[]
for i in range(n) :
    grades.append(int(input()))
    if grades[i]<38 :
        print(grades[i])
    else :
        maxi=nextmultiple(grades[i])
        if maxi-grades[i] < 3 :
            print(maxi)
        elif maxi-grades[i]==3 :
            print(grades[i])
        else :
            print(grades[i])