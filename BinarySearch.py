def BinarySearch(list1,s,l,r) :
    if(r-l==0) :
        return False
    mid=(l+r)//2
    if(s==list1[mid]) :
        return True
    if(s<list1[mid]) :
        return BinarySearch(list1,s,l,mid)
    else :
        return BinarySearch(list1,s,mid+1,r)

print(BinarySearch([1,2,3,4,6,7,8,9],4,0,9))