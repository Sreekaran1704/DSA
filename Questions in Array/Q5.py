myList=[1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
def unique(lst):
    newLst=[]
    for i in lst:
        if i in newLst:
            print(i)
            return False
        else:
            newLst.append(i)
    return True
print(unique(myList))