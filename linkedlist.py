

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=node(data)
        temp=self.head
        if self.head==None:
            self.head=newnode
        else:
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode    
    
    def insert_start(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_specific(self,data,position):
        newnode=node(data)
        temp=self.head
        if self.head==None:
            self.head=newnode
        else:
            for i in range(1,position-1):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode

    def delete_at_end(self):
            temp=self.head
            while(temp.next!=None):
                prev_temp=temp
                temp=temp.next
            prev_temp.next=None
            del(temp)
    def del_first_elemnt(self):
          temp=self.head
          self.head=self.head.next
          del(temp)      
        

    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next

L_L=linked_list()
L_L.insert(1)
L_L.insert(2)
L_L.insert(3)
L_L.insert(4)
L_L.insert(5)
L_L.insert_start(10)
L_L.delete_at_end()
L_L.insert_specific(99,3)
L_L.del_first_elemnt()

L_L.print()
