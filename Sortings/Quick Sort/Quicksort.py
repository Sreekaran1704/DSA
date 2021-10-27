def partition(customlist,low,high):
    i=low-1
    pivot=customlist[high]
    for j in range(low,high):
        if customlist[j]<=pivot:
            i+=1
            customlist[i],customlist[j]=customlist[j],customlist[i]
        else:
            customlist[i+1],customlist[high]=customlist[high],customlist[i+1]
    return i+1
def quicksort(customlist,low,high):
    if low<high:
        pi=partition(customlist,low,high)
        quicksort(customlist,low,pi-1)
        quicksort(customlist,pi+1,high)
customlist=list(map(int,input().split()))
high=len(customlist)-1
(quicksort(customlist,0,high))
print(customlist)