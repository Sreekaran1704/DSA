from array import *
arr1=array("i",[1,3,4,5,2,7])
def traversing(array):#Q1
    for i in range(len(array)):
        print(arr1[i])
traversing(arr1)#Q1

def acessing(array,index):#Q2
    if index in array:
        print(f"The element present in that index is {array[index]} ")
    else:
        print("The index is out of range")
acessing(arr1,3)#Q2

