class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)