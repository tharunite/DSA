class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def enqueue(self,value):
        new_node=Node(value)
        if self.head and self.tail is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1

    def dequeue(self):
        if self.head is None: return None
        out=self.head.val
        self.head=self.head.next
        if self.head==None:
            self.tail=None
        self.size-=1
        return out
    
    def front(self):
        if self.head is None:
            return None
        else : return self.head.val
    
    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

        