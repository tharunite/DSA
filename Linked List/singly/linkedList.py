class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def __repr__(self):
        if self.isempty():
            return "Empty Linked List"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "->".join(nodes)

    # ADD
    def append(self, value):
        if self.isempty():
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def prepend(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if self.isempty():
            print("Empty Linked List")
            return
        new = Node(value)
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1
        if current is None:
            print("Index out of Bound")
            return
        new.next = current.next
        current.next = new

    # REMOVE
    def pop(self, index=None):
        if self.isempty():
            print("Empty Linked List")
            return
        if index is None:  # pop last
            current = self.head
            if current.next is None:  # only one node
                self.head = None
                return
            while current.next.next:
                current = current.next
            current.next = None
            return
        if index == 0:  # pop head
            self.head = self.head.next
            return
        # pop at positive index
        current = self.head
        i = 0
        while current.next and i < index - 1:
            current = current.next
            i += 1
        if current.next is None:
            print("Out of Bounds")
            return
        current.next = current.next.next

    def delete(self, value):
        if self.isempty():
            print("Empty Linked List")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    remove = delete

    def delete_all(self, value):
        if self.isempty():
            print("Empty Linked List")
            return
        while self.head and self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def clear(self):
        self.head = None

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    # SEARCH
    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def index(self, value):
        if self.isempty():
            print("Empty Linked List")
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

    # CYCLE
    def has_cycle(self):
        if self.isempty():
            return False
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def cycle_start(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.data

    # UTIL
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
            print("Empty Linked List")
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data  # fixed typo (current.nextc → current.next)

    # MISC
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def mid(self):
        if self.isempty():
            print("Empty Linked List")
            return None
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def from_end(self, n):
        if self.isempty():
            print("Empty Linked List")
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


if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
