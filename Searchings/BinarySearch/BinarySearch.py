def binarySearch(list,low,high,n):
    mid1=(low+high)//2
    for i in range(len(list)):
        mid=list[mid1]
    if n==mid:
        return mid
    else:
        if n<mid:
            return binarySearch(list,low,mid,n)
        else:
            return binarySearch(list,mid+1,high-1,n)
list=list(map(int,input().split()))
high=len(list)
list.sort()
low=0
n=int(input())
print(binarySearch(list,low,high,n))