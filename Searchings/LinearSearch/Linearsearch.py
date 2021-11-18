searchingelement=int(input("Enter the element to be searched:"))
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if(i==searchingelement):
        print("Element found")
        break
    else:
        print("Element not found")
        break
