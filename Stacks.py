class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top:
            return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.bottom = Node(value)
            self.top = self.bottom
        else:
            temp = Node(value)
            self.top.next = temp
            self.top = temp
        self.length += 1
        return True

    def pop(self):
        if not self.top:
            return None
        elif self.top == self.bottom:
            pop_item = self.top.value
            self.top = None
            self.bottom = None
            self.length -= 1
            return pop_item
        else:
            current_node = self.bottom
            while True:
                if not current_node.next.next:
                    pop_item = current_node.next.value
                    self.top = current_node
                    self.top.next = None
                    break
                current_node = current_node.next
            self.length -= 1
            return pop_item

    def isempty(self):
        return self.top is None

    def __repr__(self):
        if not self.bottom:
            return str(None)
        stack_items = []
        current_node = self.bottom
        while current_node.next:
            stack_items.append(current_node.value)
            current_node = current_node.next
        stack_items.append(current_node.value)
        return str(stack_items)

    def __len__(self):
        return self.length


my_stack = Stack()
my_stack.push('google')
my_stack.push('facebook')
my_stack.push('udemy')
my_stack.push('xiaomi')
print(my_stack, len(my_stack))
