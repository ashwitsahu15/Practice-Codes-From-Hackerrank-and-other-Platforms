# import copy
# import math

# def reduced_psets(primes):
#     threshold = 0
#     for i in primes:
#         threshold += i * primes[i]

#     flop = True
#     subsets_1 = [(1, 0)]
#     subsets_2 = []

#     for prime in primes:
#         pcount = primes[prime]

#         if flop:
#             for prod, thisSum in subsets_1:
#                 max_of_this_prime = int(math.log(threshold / prod, prime))
#                 bound = min(max_of_this_prime + 1, pcount + 1)
#                 for i in range(bound):
#                     subsets_2.append((prod*(prime**i), thisSum+(prime*(pcount-i))))
#             subsets_1 = []
#         else:
#             for prod, thisSum in subsets_2:
#                 max_of_this_prime = int(math.log(threshold / prod, prime))
#                 bound = min(max_of_this_prime + 1, pcount + 1)
#                 for i in range(bound):
#                     subsets_1.append((prod*(prime**i), thisSum+(prime*(pcount-i))))
#             subsets_2 = []

#         flop = not flop

#     if flop:
#         return subsets_1
#     return subsets_2

# T = int(input())

# for test_case in range(1, T+1):
#     m = int(input())
#     primes = {}
#     for _ in range(m):
#         p,n = map(int, input().split())
#         primes[p] = n

#     ans = 0

#     ssets = reduced_psets(primes)
#     for i,j in ssets:
#         if i == j:
#             ans = max(ans, i)

#     print("Case #{}: {}".format(test_case, ans))




from fractions import Fraction

T = int(input())

for test_case in range(1, T+1):
    n,q = map(int, input().split())
    mat = [[Fraction(1,2) for _ in range(q)] for _ in range(2)]
    for _ in range(n):
        resp, score = input().split()
        score = int(score)
        for i,r in enumerate(resp):
            conf = Fraction(score,q)
            if r == 'T':
                mat[1][i] = max(mat[1][i], conf)
                mat[0][i] = max(mat[0][i], 1 - conf)
            else:
                mat[1][i] = max(mat[1][i], 1 - conf)
                mat[0][i] = max(mat[0][i], conf)

    respOpt = ""
    expectedScore = 0

    for i in range(q):
        if mat[0][i] > mat[1][i]:
            expectedScore += mat[0][i]
            respOpt += "F"
        else:
            expectedScore += mat[1][i]
            respOpt += "T"

    print("Case #{}: {} {}/{}".format(test_case, respOpt, expectedScore.numerator, expectedScore.denominator))