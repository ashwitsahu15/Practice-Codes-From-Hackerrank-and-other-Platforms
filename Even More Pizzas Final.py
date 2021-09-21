total_pizzas,team2person,team3person,team4person=[int(x) for x in input().split()]
listofpizzas=[]
for _ in range (total_pizzas):
    listofpizzas.append(input().split() [1:])
    
ans=[]

pizza_number=0
    #FIRST CASE 
while (pizza_number+2<=total_pizzas and team2person>0):
    ans.append([2,pizza_number,pizza_number+1])
    pizza_number=pizza_number+2
    team2person=team2person-1
        
    #SECOND CASE
while (pizza_number+3<=total_pizzas and team3person>0):
    ans.append([3,pizza_number,pizza_number+1,pizza_number+2])
    pizza_number=pizza_number+3
    team3person=team3person-1

    #THIRD CASE
while (pizza_number+4<=total_pizzas and team4person>0):
    ans.append ([4,pizza_number,pizza_number+1,pizza_number+2,pizza_number+3])
    pizza_number=pizza_number+4
    team4person=team4person-1

print((len(ans)),file=open("output.txt","a"))
for i in ans:
    print((' '.join([str(x) for x in i])),file=open("output.txt","a"))