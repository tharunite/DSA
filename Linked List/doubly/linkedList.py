class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ---------- Basic Utilities ----------
    def isempty(self):
        return self.head is None

    def __repr__(self):
        if self.isempty():
            return "Empty DLL"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "<->".join(nodes)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def head_value(self):
        return None if self.isempty() else self.head.data

    def tail(self):
        if self.isempty():
            print("Empty DLL")
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data

    # ---------- Adding Nodes ----------
    def append(self, value):
        new = DNode(value)
        if self.isempty():
            self.head = new
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new
        new.prev = current

    def prepend(self, value):
        new = DNode(value)
        if self.isempty():
            self.head = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if self.isempty():
            print("Empty DLL")
            return
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1
        if current is None:
            print("Out of Bounds")
            return
        new = DNode(value)
        new.next = current.next
        new.prev = current
        if current.next:
            current.next.prev = new
        current.next = new

    # ---------- Deletion ----------
    def pop(self, index=None):
        if self.isempty():
            print("Empty DLL")
            return
        # Remove last
        if index is None:
            current = self.head
            if current.next is None:  # only one node
                self.head = None
                return
            while current.next:
                current = current.next
            current.prev.next = None
            return
        # Remove head
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        # Remove at index
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        if current is None:
            print("Index out of bounds")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def delete(self, value):
        if self.isempty():
            print("Empty DLL")
            return
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # head deletion
                    self.head = current.next
                return
            current = current.next

    def delete_all(self, value):
        if self.isempty():
            print("Empty DLL")
            return
        current = self.head
        while current:
            next_node = current.next
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
            current = next_node

    def clear(self):
        self.head = None

    # ---------- Search ----------
    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def index(self, value):
        if self.isempty():
            print("Empty DLL")
            return None
        current = self.head
        i = 0
        while current:
            if current.data == value:
                return i
            current = current.next
            i += 1
        print("Not Found")
        return None

    # ---------- Reverse ----------
    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            current.prev, current.next = current.next, current.prev
            prev_node = current
            current = current.prev  # because next and prev swapped
        self.head = prev_node

    # ---------- Advanced / Optional ----------
    def mid(self):
        if self.isempty():
            print("Empty DLL")
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def from_end(self, n):
        if self.isempty():
            print("Empty DLL")
            return None
        fast = slow = self.head
        for _ in range(n):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data

    def remove_duplicates(self):
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                current = next_node
            else:
                seen.add(current.data)
                current = current.next
