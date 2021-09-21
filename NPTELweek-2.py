# def primepartition(m) :
#     for p in range(1,m) :
#         q=m-p
#         if(Isprime(p)==True and Isprime(q)==True) :
#             return True
#             break
#     else :
#         return False



# def Isprime(n) :
#     if (n <= 1) : 
#         return False
#     if (n <= 3) : 
#         return True
#     if (n % 2 == 0 or n % 3 == 0) : 
#         return False
 
#     i = 5
#     while(i * i <= n) : 
#         if (n % i == 0 or n % (i + 2) == 0) : 
#             return False
#         i = i + 6
 
#     return True


# def matched(s):
#     list_of_string=list(s)
#     for y in range(len(list_of_string)):
#         if list_of_string[y]=='(':
#             for z in range(y,len(list_of_string)):
#                 if list_of_string[z]==')':
#                     list_of_string[y]='@'
#                     list_of_string[z]='@'
#                     break
#     return('('not in list_of_string and ')'not in list_of_string)

# def rotatelist(l,k):
#     if k>len(l):
#         k=int(k%len(l))
#     return(l[k:]+l[0:k])

def mystery(l):
  l[0:2] = l[3:5]
  return()

list1 = [34,17,12,88,53,97,62]
mystery(list1)
print(list1)