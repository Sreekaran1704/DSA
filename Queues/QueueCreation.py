def create():
    queue=[]
    return queue

def enqueue(queue,element):
    queue.append(element)

def isempty(queue):
    return len(queue)==0

def dequeue(queue):
    if isempty(queue):
        return None
    else:
        return queue.pop(0)
queue=create()
for i in range(int(input("Enter the size of the queue : "))):
    enqueue(queue,input("Enter the element : "))
print("The queue is : ",queue)

for i in range(int(input("Enter the number of elements to be dequeued : "))):
    print("The element dequeued is : " ,dequeue(queue))
print("The queue is : ",queue)