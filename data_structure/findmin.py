def findmin(alist):
    min = alist[0]
    for i in alist:
        if i < min:
            min = i
    return min

print(findmin([1,2,0,1,5]))
