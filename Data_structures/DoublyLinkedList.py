class DoublyLinkedList:
    def __init__(self, initial_data):
        self.head = {
            "value": initial_data,
            "next": None,
            "prev": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "value": value,
            "next": None,
            "prev": self.tail
        }
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = {
            'value': value,
            'next': self.head,
            'prev': None
        }
        self.head['prev'] = new_node
        self.head = new_node
        self.length += 1

    def traverse(self, index: int):
        if index < 0:
            index = self.length - abs(index)
        if index > self.length or index < 0:
            raise IndexError(f'Index out of range -> Expected index: 0 to {self.length - 1} or -1 to {self.length * -1}')
        current_node = self.head
        for _ in range(index):
            current_node = current_node['next']
        return current_node

    def insert(self, index: int, value):
        if index == 0 or self.length == abs(index):
            self.prepend(value)
            return True
        if index == self.length or index == -1:
            self.append(value)
            return True
        new_node = {
            'value': value,
            'next': None,
            'prev': None
        }
        current_node = self.traverse(index - 1)
        next_node = current_node['next']
        new_node['next'] = next_node
        new_node['prev'] = current_node
        current_node['next'] = new_node
        next_node['prev'] = new_node
        self.length += 1
        return True

    def remove(self, index: int):
        if index == 0:
            self.head = self.head['next']
            self.head['prev'] = None
            self.length -= 1
            return True
        pre_node = self.traverse(index - 1)
        post_node = pre_node['next']['next']
        pre_node['next'] = post_node
        post_node['prev'] = pre_node
        self.length -= 1

    def reverse(self):
        pass

    def __repr__(self):
        my_list = []
        current_node = self.head
        while current_node:
            my_list.append(current_node['value'])
            current_node = current_node['next']
        return str(my_list)

    def __getitem__(self, item):
        return self.traverse(item)['value']

    def __len__(self):
        return self.length


if __name__ == "__main__":
    linked_list = DoublyLinkedList(10)
    linked_list.append(20)
    linked_list.prepend(12)
    linked_list.insert(0, 99)
    linked_list.insert(0, 89)
    linked_list.insert(-1, 79)
    print(linked_list, len(linked_list))
    linked_list.remove(2)
    print(linked_list, len(linked_list))
