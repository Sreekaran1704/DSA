size = int(input("Enter the size of the array: "))
l = list(map(int,input().split()))
for i in range(size-1):
    for j in range(size-1):
        if l[j+1]<l[j]:
            l[j+1],l[j]=l[j],l[j+1]
print(l)