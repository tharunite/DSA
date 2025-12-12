class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Misc
    def isempty(self):
        return self.head is None

    def __len__(self):
        if self.isempty():
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count

    def display(self):
        if self.isempty():
            print("Empty CSLL")
            return
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print("->".join(nodes) + "->(head)")

    def head_value(self):
        return None if self.isempty() else self.head.data

    def tail(self):
        if self.isempty():
            print("Empty CSLL")
            return None
        current = self.head
        while current.next != self.head:
            current = current.next
        return current.data

    #Add
    def append(self, value):
        new = CNode(value)
        if self.isempty():
            self.head = new
            new.next = new
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new
        new.next = self.head

    def prepend(self, value):
        new = CNode(value)
        if self.isempty():
            self.head = new
            new.next = new
            return
        new.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new
        self.head = new

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if self.isempty():
            print("Empty")
            return
        current = self.head
        i = 0
        while i < index - 1 and current.next != self.head:
            current = current.next
            i += 1
        if i < index - 1:
            print("Index out of bounds")
            return
        new = CNode(value)
        new.next = current.next
        current.next = new

    # Delete
    def pop(self, index=None):
        if self.isempty():
            print("Empty CSLL")
            return
        if self.head.next == self.head:
            self.head = None
            return
        if index is None:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head
            return
        if index == 0:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head
            return
        current = self.head
        i = 0
        while i < index - 1 and current.next != self.head:
            current = current.next
            i += 1
        if current.next == self.head:
            print("Index out of bounds")
            return
        current.next = current.next.next

    def delete(self, value):
        if self.isempty():
            print("Empty CSLL")
            return
        current = self.head
        prev = None
        while True:
            if current.data == value:
                if prev is None:  
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = current.next
                    tail.next = self.head
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def delete_all(self, value):
        if self.isempty():
            print("Empty CSLL")
            return
        current = self.head
        prev = None
        while True:
            next_node = current.next
            if current.data == value:
                if prev is None: 
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = current.next
                    tail.next = self.head
                    current = self.head
                    if self.head == next_node:  
                        break
                    continue
                else:
                    prev.next = current.next
            else:
                prev = current
            current = next_node
            if current == self.head:
                break

    def clear(self):
        self.head = None

    #search
    def __contains__(self, value):
        if self.isempty():
            return False
        current = self.head
        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def index(self, value):
        if self.isempty():
            print("Empty CSLL")
            return None
        current = self.head
        i = 0
        while True:
            if current.data == value:
                return i
            current = current.next
            i += 1
            if current == self.head:
                break
        print("Not Found")
        return None

    #Reverse
    def reverse(self):
        if self.isempty() or self.head.next == self.head:
            return
        prev = None
        current = self.head
        start = self.head
        while True:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            if current == start:
                break
        self.head.next = prev
        self.head = prev


    def mid(self):
        if self.isempty():
            print("Empty CSLL")
            return None
        slow = fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def from_end(self, n):
        if self.isempty():
            print("Empty CSLL")
            return None
        length = len(self)
        if n > length:
            return None
        current = self.head
        for _ in range(length - n):
            current = current.next
        return current.data

    def remove_duplicates(self):
        if self.isempty() or self.head.next == self.head:
            return
        seen = set()
        current = self.head
        prev = None
        start = self.head
        while True:
            if current.data in seen:
                prev.next = current.next
                current = current.next
            else:
                seen.add(current.data)
                prev = current
                current = current.next
            if current == start:
                break
