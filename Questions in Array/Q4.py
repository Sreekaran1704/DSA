import numpy as np
myArray=np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def maxProduct(lst):
    product=0
    for i in range(len(myArray)):
        for j in range(i+1,len(myArray)):
            if i==j:
                continue
            elif lst[i]*lst[j]>product:
                product=lst[i]*lst[j]
                pairs=str(lst[i])+" "+str(lst[j])
    print(pairs)
    print(product)
maxProduct(myArray)

