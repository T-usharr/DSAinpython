# # Stack with Array
# array=[]
# top=-1
# n=5
# def push(data):
#     global top
#     if(top>n):
#         print("OVERfLOW")
#     else:
#         top+=1
#         array[top]=(data)
# def empty():
#     global top
#     if(top<=-1):
#         return True
#     else:
#         return False    
# def pop():
#     global top
#     if(empty()):
#         print("Empty stack")
#     else:
#         print("Popped Element:",array[top])
#         top-=1
# def top():
#     global top
#     if(empty()):
#         print("Empty stack")
#     else:
#         print("Top Element:",array[top])
# def show():
#     global top
#     if(empty()):
#         print("Empty stack")
#     else:
#         while(top!=0):
#             print(array[top])
#             top=top-1
# push(1)            
# push(2)            
# push(3)            
# push(4)            
# push(5)            
# push(6)
# show()

## Stack with LinkedList
class node:
    def __init__(self,data):
        self.data = data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None 
    def push(self,data): #front push
        newnode= node(data)
        newnode.next=self.head
        self.head=newnode
    def pop(self): #pop from front
        if(self.head==None):
            print("Stack is empty")
        else:
            temp= self.head
            print("Popped Elment is: ",temp.data)
            self.head=self.head.next
            del(temp)    
    def top(self): #head data
        if(self.head==None):
            print("Stack is empty")
        else:
            print("Top- ",self.head.data)
    def show(self):
         if(self.head==None):
                print("Stack is empty")
         else:
            print("Stack")
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next
st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.pop()
st.top()
st.show()