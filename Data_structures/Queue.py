class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first:
            return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if not self.first:
            return None
        dequeue_item = self.first
        self.first = self.first.next
        self.length -= 1
        if not self.first:
            self.last = None
        return dequeue_item.value

    def isempty(self):
        return self.first is None

    def __repr__(self):
        stack_items = []
        current_node = self.first
        while current_node:
            stack_items.append(current_node.value)
            if not current_node.next:
                break
            current_node = current_node.next
        return str(stack_items)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    my_stack = Queue()
    my_stack.enqueue('google')
    my_stack.enqueue('facebook')
    my_stack.enqueue('amazon')
    my_stack.enqueue('netflix')
    my_stack.dequeue()
    print(my_stack.peek())
    print(my_stack, len(my_stack))
