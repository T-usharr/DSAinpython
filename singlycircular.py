class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CQLL:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        newnode=node(data)
        if(self.head==None):
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
    def deque(self):
           temp=self.head
           self.head=self.head.next
           del(temp)

    def print(self):
        temp=self.head
     
        while(temp.next!=self.head):
            print(temp.data,end=" ")
            temp=temp.next
            
circular_queue=CQLL()
circular_queue.enqueue(1)            
circular_queue.enqueue(2)            
circular_queue.enqueue(3)            
circular_queue.enqueue(4)            
circular_queue.enqueue(5)            
circular_queue.deque()            

circular_queue.print()   
       
