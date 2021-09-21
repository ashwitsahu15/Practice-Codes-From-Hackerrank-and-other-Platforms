vowels=["A", "O", "Y", "E", "U", "I","a","o","y","e","u","i"]
s=input()
s=s.lower()
s=(list(s))
s=[x for x in s if x not in vowels]
for i in s :
    print('.'+i,end="")