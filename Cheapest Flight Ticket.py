A=int(input())
B=int(input())
C=int(input())
D=int(input())
ans=[x for x in range(B) if x<=(B-A) and x>=C and x%D==0]
print(len(ans))