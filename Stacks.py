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
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.top:
            return None
        pop_item = self.top.value
        self.top = self.top.next
        self.length -= 1
        return pop_item

    def isempty(self):
        return self.top is None

    def __repr__(self):
        stack_items = []
        current_node = self.top
        while current_node:
            stack_items.append(current_node.value)
            if not current_node.next:
                break
            current_node = current_node.next
        return str(stack_items)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('google')
    my_stack.push('facebook')
    my_stack.push('udemy')
    my_stack.push('xiaomi')
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.push(100)
    print(my_stack, len(my_stack))
