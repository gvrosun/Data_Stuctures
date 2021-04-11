class HashTable:
    def __init__(self, size: int):
        if size < 1:
            raise IndexError('Size of hashtable should be minimum 1')
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        hash_data = 0
        for i in range(len(key)):
            hash_data = (hash_data + ord(key[i]) * i) % self.size
        return hash_data

    def __setitem__(self, key, value):
        if not (None in self.data):  # Checking self.data != None
            raise IndexError('Exceeding hashtable limit')
        pointer = self._hash(key)
        if not self.data[pointer]:
            self.data[pointer] = []
        else:
            i = 0
            for k, v in self.data[pointer]:
                if k == key:
                    self.data[pointer][i][1] = value
                    return True
                i += 1
        self.data[pointer].append([key, value])
        return True

    def __getitem__(self, key):
        pointer = self._hash(key)
        items = self.data[pointer]
        if items:
            for k, v in items:
                if k == key:
                    return v
        return False

    def __repr__(self):
        my_set = set()
        for items in self.data:
            if items:
                for single_item in items:
                    data_element = "{key}: {value}".format(key=single_item[0], value=single_item[1])
                    my_set.add(data_element)
        return str(my_set)

    def items(self) -> list:
        """
        Returns list of tuples contains [(key, value), ...]
        :return: list
        """
        hashtable_items = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_items.append(tuple(item_data))
        return hashtable_items

    def keys(self) -> list:
        """
        Returns list of keys
        :return: list
        """
        hashtable_keys = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_keys.append(item_data[0])
        return hashtable_keys

    def values(self) -> list:
        """
        Returns list of values
        :return: list
        """
        hashtable_keys = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_keys.append(item_data[1])
        return hashtable_keys

    def delete(self, key) -> bool:
        """
        Delete an element using key
        :param key: key
        :return: bool
        """
        for items in self.data:
            if items:
                for item_data in items:
                    if item_data[0] == key:
                        index = self.data.index(items)
                        self.data[index].remove(item_data)
                        return True
        return False


if __name__ == '12':
    my_hashtable = HashTable(5)
    my_hashtable['hello'] = 'hi'
    my_hashtable['hello'] = 'hii'
    my_hashtable['data'] = 'hello'


def first_recurring_number_using_dict(list_data: list) -> int:
    my_dict = {}
    for item in list_data:
        if my_dict.get(item):
            return item
        else:
            my_dict[item] = True


def first_recurring_number_using_for(list_data: list) -> int:
    result = None
    start_index = 0
    end_index = len(list_data) - 1
    while start_index < end_index:
        i = start_index + 1
        while i <= end_index:
            if list_data[start_index] == list_data[i]:
                result = list_data[start_index]
                end_index = i - 1
                print('Hi: ', start_index, end_index)
                continue
            i += 1
        start_index += 1
    return result


my_list = [2, 5, 9, 12, 6, 6, 9, 2]
print(first_recurring_number_using_for(my_list))
print(first_recurring_number_using_dict(my_list))
