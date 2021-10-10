from array import *
arr1=array('i',[1,2,3,4,5])
n=int(input())
def acessing(arr1,n):
    if n>len(arr1):
        print("The choosen index is out of the range")
    else:
        print(arr1[n])
acessing(arr1,n)
