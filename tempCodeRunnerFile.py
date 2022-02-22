class node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None
class doubly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None 
   
    def insert(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=self.tail=newnode
        else:
           self. tail.next=newnode
           newnode.prev=self.tail
           self.tail=newnode
   
    def show (self) :
        temp=self.tail
        while(temp!=head):
            print(temp.data)
            temp=temp.prev    

DL=doubly_linkedlist()
DL.insert(1)
DL.insert(2)
DL.insert(3)
DL.insert(4)
DL.insert(5)
DL.show()