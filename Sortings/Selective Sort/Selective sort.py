def selctiveSort(arr,size):
    for i in range(size):
        min_index=i
        for  j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
size=int(input("Enter the size of array : "))
arr=list(map(int,input("Enter the elements of the array : ").split()))
print(arr)
selctiveSort(arr,size)
print("After sorting")
print(arr)