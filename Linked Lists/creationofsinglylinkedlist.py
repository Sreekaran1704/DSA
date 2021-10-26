class node:
	def __init__(self,value=None,next=None):
		self.value=value
		self.next=next
class SlinkedList:
	def __init__(self):
		self.head=None
	def createList(self):
		n=int(input("Enter the size of Linked List : "))
		for i in range(n):
			data=int(input())
			newnode=node(data)
			if self.head==None:
				self.head=newnode
			else:
				temp=self.head
				while(temp.next!=None):
					temp=temp.next
				temp.next=newnode
	def printList(self):
		for i in range(self.n):
			print()

