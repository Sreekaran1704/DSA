# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def createList(self, data):
    newNode = Node(data)
    if(self.head!=None):
      temp = self.head
      while(temp.next!=None):
        temp = temp.next
      temp.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    temp= self.head
    while(temp!=None):
      print(temp.data)
      temp = temp.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
for i in range(int(input())):
	a=int(input())
	LL.createList(a)
print("The elements in the list are : ")
LL.printLL()