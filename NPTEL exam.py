# def quicksortbad(l):
#   if len(l) < 2:
#     return(l)
#   else:
#     pivot = l[0]
#     smaller = [l[j] for j in range(1,len(l)) if l[j] < pivot]
#     bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
#     rearrange = quicksortbad(smaller) + [pivot] + quicksortbad(bigger)
#     return(rearrange)
# print(quicksortbad([1,5,4,4,5,6,7,7,91,12,13,14]))

# def median3(x,y,z):
#     if x <= y:
#         if x >= z:
#             return x
#     if y<=z: 
#         if y>=x: 
#             mymedian=y 
#     if z<=x: 
#         if z>=y: 
#             mymedian=z
    
#     return(mymedian)

# print(median3(1,2,3))
# print(median3(3,1,2))
# ans=[]
# for i in range(1,3000) :
#     for a in range(1,10) : 
#         for b in range(1,10) : 
#             for c in range(1,10) : 
#                 if i==((a*a*a)+(b*b*b)+(c*c*c)) :
#                     ans.append(i)
# ans=list(set(ans))
# ans.sort()
# print(ans)

# l1=[3, 10, 17, 24, 29, 36, 43, 55, 62, 66, 73, 80, 81, 92, 99, 118, 127, 129, 134, 136, 141, 153, 155, 160, 179, 190, 192, 197, 216, 218, 225, 232, 244, 251, 253, 258, 270, 277, 281, 288, 307, 314, 342, 344, 345, 349, 352, 359, 368, 371, 375, 378, 397, 405, 408, 415, 433, 434, 440, 459, 466, 469, 471, 476, 495, 496, 514, 521, 528, 532, 540, 547, 557, 560, 566, 567, 577, 584, 586, 593, 603, 623, 638, 640, 645, 648, 664, 684, 687, 694, 701, 713, 729, 731, 736, 738, 745, 750, 755, 757, 762, 764, 775, 783, 792, 794, 801, 811, 820, 853, 855, 856, 857, 862, 863, 881, 882, 902, 918, 919, 944, 946, 953, 972, 979, 980, 1009, 1025, 1029, 1032, 1051, 1070, 1071, 1073, 1080, 1088, 1099, 1136, 1149, 1161, 1197, 1198, 1240, 1242, 1249, 1268, 1288, 1305, 1366, 1367, 1415, 1457, 1459, 1466, 1485, 1522, 1536, 1583, 1584, 1674, 1753, 1801, 1970, 2187]



# def aboveaverage(l):
#     d = {}
#     for i in l:
#         name, score = i
#         if name in d:
#             tot_score, num = d[name]
#             d[name] = (tot_score+score, num+1)
#         else:
#             d[name] = (score, 1)
#     max= -1
#     for k in d:
#         tot_score, num = d[k]
#         ave = tot_score/num
#         if(max < ave):
#             max = ave
#     l = []
#     for k in d:
#         tot_score, num = d[k]
#         ave = tot_score/num
#         if(max == ave):
#             l.append(k)
#     l.sort()
#     return l



def prevPermutation(str):
 
    # Find index of the last element
    # of the string
    n = len(str) - 1
 
    # Find largest index i such that
    # str[i - 1] > str[i]
    i = n
    while (i > 0 and str[i - 1] <= str[i]):
        i -= 1
 
    # if string is sorted in ascending order
    # we're at the last permutation
    if (i <= 0):
        return False
 
    # Note - str[i..n] is sorted in
    # ascending order
 
    # Find rightmost element's index
    # that is less than str[i - 1]
    j = i - 1
    while (j + 1 <= n and
           str[j + 1] <= str[i - 1]):
        j += 1
 
    # Swap character at i-1 with j
    str = list(str)
    temp = str[i - 1]
    str[i - 1] = str[j]
    str[j] = temp
    str = ''.join(str)
 
    # Reverse the substring [i..n]
    str[::-1]
 
    return True, str
 
 

if __name__ == '__main__':
    str = "ghadbicefj"
 
    b, str = prevPermutation(str)
 
    if (b == True):
        print("Previous permutation is", str)
    else:
        print("Previous permutation doesn't exist")
prevPermutation('ghadbicefj')