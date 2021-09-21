# for i in range(int(input())) :
#     n=int(input())
#     l=[int(x) for x in input().split()]
#     ans=0
#     sum0=0
#     flag = 0
#     if sorted(l,reverse=True)==l:
#         flag=1
#     for a in range(0,n-1) :
#         if(flag):
#             sum0 = n+n-2
#             break
#         b=l.index(min(l[a:]))
#         sum0=b-a+1+sum0
#         l2=l[a:b+1]
#         l2.reverse()
#         l=l[:a]+l2+l[b+1:]
#     print("Case #"+str(i+1)+": "+str(sum0))


for i in range(int(input())) :
    n=int(input())
    l=[int(x) for x in input().split()]
    cost=0
    for a in range(0,n-1):
        b=l.index(min(l[a:]))+1
        l[a:b]=reversed(l[a:b])
        ans=ans+b-a
    print("Case #"+str(i+1)+": "+str(ans))





# 2nd Program


# for k in range(int(input())):
#     l=[x for x in input().split()]
#     a,b=int(l[0]),int(l[1])
#     s=list(l[2])
#     flag=0
#     for i in range(len(s)):
#         if i==0 and s[i]=='?':
#             flag=1 
#             continue
#         elif flag==1 and s[i]=='?':
#                 continue
#         elif flag==1 and s[i]!='?':
#             for j in range(i,-1,-1):
#                 s[j]=s[i]
#             flag=0    
#         elif s[i]=='?' and flag==0:
#                 s[i]=s[i-1]
#     cost=0        
#     for i in range(len(s)-1):
#         if (s[i]=='C' and s[i+1]=='J'):
#             cost+=a 
#         elif (s[i]=='J' and s[i+1]=='C'):
#             cost+=b 
#     print("Case #"+str(k+1)+':',cost)



# for i in range(int(input())) :
#     n,c=[int(x) for x in input().split()]
#     if c<n-1 :
#         print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
#     else :
#         l=[x for x in range(1,n+1)]
#         a=0
#         while c>0 and a<n-1:
#             for b in range(1,len(l)) :
#                 if b-a<=c :
#                     break
#             l[a:b]=reversed(l[a:b])
#             a+=1
#             c=c-len(l[a:b])
#         print("Case #"+str(i+1)+": "+str(l))



# def createL(n):
#     l = [x for x in range(1,n+1)]
#     return l 

# def operationL(n,p):
#     if p < n-1:
#         return []
#     l = []
#     t = 0 
#     c = 1
#     for i in range(n-1, 0, -1):
#         c += 1

#         if t+c+i-1 >= p:
#             r = p-t-i+1
#             l.append(r)
#             for k in range(i-1):
#                 l.append(1)
#             t = p
#             break

#         t += c 
#         l.append(c)
#     if t<p:
#         return []
#     return l

# def operate(l, opeL):
#     length = len(opeL)
#     for i in range(length):
#         t = len(l)-(i+2)
#         sp = t+opeL[i]
#         l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
#     return l 

# def solve():
#     inp = input().split()
#     n = int(inp[0])
#     p = int(inp[1])
#     l = createL(n)
#     opeL = operationL(n,p)
#     l = operate(l, opeL)
#     result = ""
#     if opeL:
#         for item in l:
#             result += str(item)+ " "
#     else:
#         result ="IMPOSSIBLE"
#     print("Case #"+str(i+1)+": "+ str(result))

# for i in range(int(input())):
#     solve()

# #include<bits/stdc++.h>
# using namespace std;
# int Reversort(vector<int>v ,int n){
#     int x=n;
#     vector<pair<int ,int>>p;
#     for(int i=1;i<x;i++){
#         p.push_back(make_pair(v[i],i));
#     }
#     int count=0;
#     int k=1;
#     int j=0;
#     for(int i=1;i<p.size();i++){
        
#         if(i<p.size()){
#         int u=(p[i-1].second);
#         int j=u+1;
#         reverse(v.begin()+k, v.begin()+j);
        
#         k++;
#       count=count+i;  
#         }
        
#     }
# return count;
# }

# int main(){
# int t;
# cin>>t;
# while(t--){
    
#     int x,y;
#     cin>>x;
#     y=x+1;
#     vector<int>v;
    
#     for(int i=1;i<y;i++){
#         int z;cin>>z;
#         v.push_back(z);
        
#     }
    
#     cout<<Reversort(v,y)<<endl;
# }



# return 0;}




# import sys
# import random

# T = 100
# Ns = (10, 50, 50)
# Qs = (30000, 30000, 17000)
# CORRECT, WRONG = 1, -1


# def GenCase(n):
#   r = list(range(1, n + 1))
#   random.shuffle(r)
#   return tuple(r)


# def GenCases(n):
#   return tuple(GenCase(n) for _ in range(T))


# class Error(Exception):
#   pass


# class JudgeError(Exception):
#   pass


# INVALID_LINE_ERROR = "Couldn't read a valid line"
# TOO_LONG_LINE_ERROR = "Line too long: {} characters".format
# WRONG_NUM_TOKENS_ERROR = "Wrong number of tokens, expected 3 or {} got {}".format
# NOT_INTEGER_ERROR = "Not an integer: {}".format
# OUT_OF_BOUNDS_ERROR = "{} is out of bounds".format
# REPEATED_INTEGERS_ERROR = "Received repeated integers: {}".format
# TOO_MANY_QUERIES_ERROR = "Queried too many times"
# WRONG_ORDER_ERROR = "Guessed wrong order"
# CASE_ERROR = "Case #{} failed: {}".format
# EXCEPTION_AFTER_END_ERROR = (
#     "Exception raised while reading input after all cases finish.")
# ADDITIONAL_INPUT_ERROR = "Additional input after all cases finish: {}".format
# QUERIES_USED = "Total Queries Used: {}/{}".format


# def ParseInteger(line):
#   try:
#     return int(line)
#   except:
#     raise Error(NOT_INTEGER_ERROR(line))


# def ReadValues(n, line):
#   if len(line) > 1000:
#     raise Error(TOO_LONG_LINE_ERROR(len(line)))
#   parts = line.split()
#   if len(parts) not in (3, n):
#     raise Error(WRONG_NUM_TOKENS_ERROR(n, len(parts)))
#   v = tuple(ParseInteger(parts[i]) for i in range(len(parts)))
#   for vi in v:
#     if not 1 <= vi <= n:
#       raise Error(OUT_OF_BOUNDS_ERROR(vi))
#   if len(set(v)) != len(v):
#     raise Error(REPEATED_INTEGERS_ERROR(v))
#   return v


# def Inv(v):
#   r = list(v)
#   for i in range(len(r)):
#     r[v[i] - 1] = i + 1
#   return tuple(r)


# def Mid(pos, v):
#   if len(v) != 3:
#     raise JudgeError("Mid called with {} values (expected 3)".format(len(v)))
#   p = tuple(pos[vi - 1] for vi in v)
#   min_p, max_p = min(p), max(p)
#   for vi in v:
#     if pos[vi - 1] not in (min_p, max_p):
#       return vi


# def Output(line):
#   try:
#     print(line)
#     sys.stdout.flush()
#   except:
#     # If we let stdout be closed by the end of the program, then an unraisable
#     # broken pipe exception will happen, and we won't be able to finish
#     # normally.
#     try:
#       sys.stdout.close()
#     except:
#       pass


# def RunCase(case, max_q):

#   def Input():
#     try:
#       return input()
#     except:
#       raise Error(INVALID_LINE_ERROR)

#   pos = Inv(case)
#   q = 0
#   while True:
#     v = ReadValues(len(case), Input())
#     if len(v) == len(case):
#       if v != case and v != tuple(reversed(case)):
#         raise Error(WRONG_ORDER_ERROR)
#       return q
#     if q >= max_q:
#       raise Error(TOO_MANY_QUERIES_ERROR)
#     q += 1
#     Output(Mid(pos, v))


# def RunCases(cases, max_q):
#   Output("{} {} {}".format(len(cases), len(cases[0]), max_q))
#   tot_q = 0
#   for i, case in enumerate(cases, 1):
#     try:
#       q = RunCase(case, max_q - tot_q)
#       Output(CORRECT)
#       tot_q += q
#     except Error as err:
#       Output(WRONG)
#       raise Error(CASE_ERROR(i, err))

#   try:
#     extra_input = input()
#   except EOFError:
#     return tot_q
#   except Exception:  # pylint: disable=broad-except
#     raise Error(EXCEPTION_AFTER_END_ERROR)
#   raise Error(ADDITIONAL_INPUT_ERROR(extra_input[:100]))


# def main():
#   assert len(sys.argv) == 2, "Bad usage"
#   index = int(sys.argv[1])
#   random.seed(1234 + index)
#   assert index in (0, 1, 2)
#   try:
#     q = RunCases(GenCases(Ns[index]), Qs[index])
#     print(QUERIES_USED(q, Qs[index]), file=sys.stderr)
#   except Error as err:
#     print(str(err)[:1000], file=sys.stderr)
#     sys.exit(1)
#   except Exception as exception:
#     Output(WRONG)
#     print(
#         ("JUDGE_ERROR! Internal judge exception: {}".format(exception))[:1000],
#         file=sys.stderr)
#     sys.exit(1)


# # if __name__ == "__main__"
# #   main()






# import time
# # from itertools import permutations  

# t,n,q=[int(x) for x in input().split()]
# l=[w for w in range(1,n)]
# start_time = time.time()
# for _ in range(t) :
#     # perm = permutations(range(1,11)) 
#     # for i in list(perm): 
#     #     print(list(i))
#     # code



# import sys
# # O(n * k) solution for finding
# # maximum sum of a subarray of size k
# INT_MIN = -sys.maxsize - 1
 
# # Returns maximum sum in a
# # subarray of size k.
 
 
# def maxSum(arr, n, k):
 
#     # Initialize result
#     max_sum = INT_MIN
 
#     # Consider all blocks
#     # starting with i.
#     for i in range(n - k + 1):
#         current_sum = 0
#         for j in range(k):
#             current_sum = current_sum + arr[i + j]
 
#         # Update result if required.
#         max_sum = max(current_sum, max_sum)
 
#     return max_sum
 
 
# # Driver code
# # arr = [1, 4, 2, 10, 2,
# #        3, 1, 0, 20]
# # k = 4
# # n = len(arr)
# # print(maxSum(arr, n, k))
# print("--- %s seconds ---" % (time.time() - start_time))



