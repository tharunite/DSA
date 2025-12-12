class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def search(self, item):
        return item in self.items

    def traverse(self):
        for item in reversed(self.items):
            print(item)

    def __repr__(self):
        return "Stack(top -> bottom): " + " -> ".join(map(str, reversed(self.items)))


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack.size())
    print(stack.is_empty())
    stack.traverse()
    stack.clear()
    print(stack.is_empty())
