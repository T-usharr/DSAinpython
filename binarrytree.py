
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def inorder(root):
    if(root==None):
        return
    else:
        inorder(root.left) 
        print(root.data,end=' ')
        inorder(root.right)    

def preorder(root):
    if(root==None):
        return
    else:
        print(root.data,end=' ')
        preorder(root.left) 
        preorder(root.right)    

def postorder(root):
    if(root==None):
        return
    else:
        postorder(root.left) 
        postorder(root.right)    
        print(root.data,end=' ')

root=node(1)            
root.left=node(2)            
root.right=node(3)            
root.left.left=node(4)            
root.right.right=node(5)
inorder(root)            