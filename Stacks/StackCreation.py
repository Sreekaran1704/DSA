def creation ():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)

def pop(stack):
    return stack.pop()

n=int(input("Enter the number of numbers you want to push : "))
stack=creation()
for i in range(n):
    item=int(input("Enter the number : "))
    push(stack,item)
print("The stack is : ",stack)

n1=int(input("Enter the number of numbers you want to pop : "))
for i in range(n1):
    pop(stack)
print("The stack after popping is : ",stack)
