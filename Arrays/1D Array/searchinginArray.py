from array import *
arr1=array('i',[1,2,3,4,5])
def searching(array,element):
    if element in array:
        print(f"It is present at the index {array[element]}")
    else:
        print("It is not present in the array")
searching(arr1,4)