def permutation(lst1,lst2):
    if len(lst1)!=len(lst2):
        return False
    else:
        lst1.sort()
        lst2.sort()
        if lst1==lst2:
            return True
        else:
            return False
list1=[1,2,3]
list2=[2,3,1]
print(permutation(list1,list2))