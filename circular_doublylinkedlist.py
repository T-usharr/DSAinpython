class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Circular_DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail= None
  
    def insert(self,data):
        newnode=node(data)
        if(self.head==None):
            self.head=self.tail=newnode
            self.head.next=self.head      
            self.head.prev=self.head
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            newnode.next=self.head
            self.head=newnode
            self.tail=newnode
   
    def print(self):
        temp=self.head
        if(self.head==None):
            print("Empty")
        else:
            #  while True:
            #     print(temp.data, end = ' ')
            #     temp= temp.next
            #     if temp == self.head:
            #         break
            while(temp.next!=self.head):
                print(temp.data,end="")
                temp=temp.next

CDL=Circular_DoublyLinkedList()
CDL.insert(1)          
CDL.insert(2)          
CDL.insert(3)          
# CDL.insert(4)          
# CDL.insert(5)
CDL.print()          