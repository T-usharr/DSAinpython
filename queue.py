    
# #Queue with linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):#  append data
        newnode=node(data)
        if(self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
  
    def deque(self):#pre del
        temp=self.head
        if(self.head==None):
            print("Empty Queue")
        else:
            temp=self.head
            print("Poped elemnt is-> ",self.head.data)
            self.head=self.head.next
            del(temp)

    def top(self):
        if(self.head==None):
            print("Empty Queue")
        else:
            print("Top elemnt is-> ",self.head.data)
    def show(self):
        temp=self.head
        if(self.head==None):
            print("Empty Queue")
        else:
            print("Queue")
            while(temp!=None):
                print(temp.data)
                temp=temp.next
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.deque()
q.deque()
q.deque()
q.top()
q.show()


