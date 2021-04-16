class Stack:
    def __init__(self):
        self.data = []

    def peek(self):
        if self.data:
            return self.data[-1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.data:
            return self.data.pop()

    def isempty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('google')
    my_stack.push('amazon')
    print(my_stack.peek())
    print(my_stack, len(my_stack))
    print(my_stack.pop())
    print(my_stack, len(my_stack))
    print(my_stack.isempty())
    my_stack.pop()
    print(my_stack.isempty())
    my_stack.pop()
