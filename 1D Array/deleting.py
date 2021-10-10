from array import *
arr1=array("i",[1,2,3,4,5])
def deleting(array,ele):
    if ele in array:
        arr1.remove(ele)
        print(array)
deleting(arr1,3)