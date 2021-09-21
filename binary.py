n=int(input())
bi=bin(n)
bi = bi[2 : : ] 
con=map(len, bi.split('0'))
maxi=max(con)
print(maxi)
