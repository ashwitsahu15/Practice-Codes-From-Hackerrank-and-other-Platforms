# #Function that prints the solution to send to the judge
# def printsolution(deliveries):
    
#     # We print number of shipments
#     print(len(deliveries))
#     for between in deliveries:
#         #We print each shipment generating a string and finally printing it
#         #First, we put the shipment if it goes to a group of 4, 3 or 2
#         cad=str(between[0])
#         # We will go through the list to print which pizzas were in that shipment
#         for element in between[1:]:
#             cad = cad + "" + str (element)
#         #We print the solution
#         print (cad)


#Main program
def main ():
    # We declare variables to read total pizzas and total of each type of equipment
    # nPizzas = 0
    # nEq2 = 0
    # nEq3 = 0
    # nEq4 = 0
    # We read number of pizzas, teams of 2, 3 and 4 members
    nPizzas,nEq2,nEq3,nEq4=[int(x) for x in input().split()]
    # We declare a list with the pizzas that we will read
    pizzas=[]
    # We read all the pizzas. We put them in a list each, ignoring the first element
    # The reason for ignoring the first element is that it tells us how many ingredients there are, but for
    # save space we do not put it and we can always calculate with the "len" function
    for _ in range (nPizzas):
        pizzas.append(input().split() [1:])

    #List that will contain the result of assigned pizzas
    res=[]

    #As long as there are Pizzas and groups left, I create deliveries
    currentpizza = 0

   #First groups of 2
    while (currentpizza + 2 <= nPizzas and nEq2> 0):
        res.append ([2, currentpizza, currentpizza + 1])
        currentpizza = currentpizza + 2
        nEq2 = nEq2-1

    print(res)
        
    #Then groups of 3
    while (currentpizza + 3 <= nPizzas and nEq3> 0):
        res.append ([3, currentpizza, currentpizza + 1, currentpizza + 2])
        currentpizza = currentpizza + 3
        nEq3 = nEq3-1
    print(res)

    #We assign pizzas last to groups of 4
    while (currentpizza + 4 <= nPizzas and nEq4> 0):
        # Add the result
        res.append ([4, currentpizza, currentpizza + 1, currentpizza + 2, currentpizza + 3])
        currentpizza = currentpizza + 4
        nEq4 = nEq4-1
 
    print(res)

    #print the result of res
    # printsolution(res)
    for i in res :
        print(' '.join([str(x) for x in i]))




# Code to execute initial
main()