# FIXME:Delete function

class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def insert(root,data):
    if root==None:
        return node(data)
    else:
        if(root.data==data):
            return root
        elif(root.data>data):
            root.left=insert(root.left,data)
        
        elif(root.data<data):
            root.right=insert(root.right,data)
        return root
def maxnode(root):
    temp=root
    while(temp.right!=None):
        temp=temp.right
    return temp    

def delete_node(root,data):
    if(root==None):
        return root
    elif(root.data<data):
        root.right=delete_node(root.right,data)    
    elif(root.data>data):
        root.left=delete_node(root.left,data)    
    else:
        if(root.left==None and root.right==None):
            del(root)
            root=None
            return root
        elif(root.left==None ):
            temp1=root
            root=root.right
            del(temp1)
            return root    
        elif(root.right==None ):
            temp2=root
            root=root.left
            del(temp2)
            return root    
        else:
            temp3=maxnode(root.left)    
            root.data=temp3.data
            root.left=delete_node(root.left,temp3.data)

def search(root,data):
    if(root.data==data or root==None):
        return root.data
    elif(root.data<data):
        root.right= search(root.right,data)
    elif(root.data>data):
        root.left= search(root.left,data)    
    else:
        print("Not found")
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

root=node(50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
# delete_node(root,20)
inorder(root)
print("\n")
preorder(root)
print("\n")
postorder(root)
search(root,70)