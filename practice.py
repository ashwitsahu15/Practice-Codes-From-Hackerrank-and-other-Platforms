t=int(input())
for item in range(t) :
    s = input()
    even = ""
    odd = ""
    for _ in range(len(s)) :
        if _ % 2 == 0 :
            even = even + s[_] 
        else:
            odd = odd + s[_]
    print(even,odd)