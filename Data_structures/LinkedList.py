class LinkedList:
    def __init__(self, initial_data):
        self.head = {
            "value": initial_data,
            "next": None
        }
        self.tail = self.head
        self._length = 1

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail["next"] = new_node
        self.tail = new_node
        self._length += 1

    def prepend(self, value):
        new_node = {
            'value': value,
            'next': self.head
        }
        self.head = new_node
        self._length += 1

    def traverse(self, index: int):
        if index < 0:
            index = self._length - abs(index)
        if index > self._length or index < 0:
            raise IndexError(f'Index out of range -> Expected index: 0 to {self._length - 1} or -1 to {self._length * -1}')
        current_node = self.head
        for _ in range(index):
            current_node = current_node['next']
        return current_node

    def insert(self, index: int, value):
        if index == 0 or self._length == abs(index):
            self.prepend(value)
            return True
        if index == self._length or index == -1:
            self.append(value)
            return True
        new_node = {
            'value': value,
            'next': None
        }
        current_node = self.traverse(index - 1)
        next_node = current_node['next']
        new_node['next'] = next_node
        current_node['next'] = new_node
        self._length += 1
        return True

    def remove(self, index: int):
        if index == 0:
            self.head = self.head['next']
            return True
        pre_node = self.traverse(index - 1)
        post_node = pre_node['next']['next']
        pre_node['next'] = post_node
        self._length -= 1

    def reverse(self):
        if self._length == 1:
            return None
        first_node = self.head
        second_node = first_node['next']
        self.tail = self.head
        while second_node:
            third_node = second_node['next']
            second_node['next'] = first_node
            first_node = second_node
            second_node = third_node
        self.head['next'] = None
        self.head = first_node

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
        return self._length


if __name__ == "__main__":
    linked_list = LinkedList(10)
    linked_list.append(20)
    linked_list.prepend(12)
    linked_list.insert(1, 99)
    print(linked_list, len(linked_list))
    linked_list.reverse()
    print(linked_list, len(linked_list))
