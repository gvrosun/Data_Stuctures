my_array = ['a', 'b', 'c', 'd']
print(my_array)

my_array.append('z')  # O(1)
my_array.pop()  # O(1)
my_array.insert(0, 'z')  # O(n)
my_array.insert(2, 'm')  # O(n/2) => O(n)
my_array.remove('c')  # O(n)

# print(my_array)


# Creating own array
class Array:
    def __init__(self, data=None):
        self.length = 0
        self.data = {}
        if data:
            for item in data:
                self.data[self.length] = item
                self.length += 1

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item_to_delete = self.data[index]
        self.shift_items(index)
        return item_to_delete

    def shift_items(self, index):
        for _index in range(index, self.length - 1):
            self.data[_index] = self.data[_index + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def show(self):
        return [data for data in self.data.values()]

    def __repr__(self):
        return "{0}".format(list(self.data.values()))

    def __len__(self):
        return len(self.data.values())

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value


my_array = Array([1, 2, 3])
my_array.push(10)
my_array.push('Rosun')
my_array.push('Vin')
my_array.push(False)
my_array.pop()
my_array.delete(0)
my_array[1] = 'Vin1'


# Reverse a string
class InvalidInputError(Exception):
    pass


def reverse_string(string: str) -> str:
    reversed_string = ''
    if not isinstance(string, str):
        raise InvalidInputError("string should be for type str")
    elif len(string) < 2:
        raise InvalidInputError("String length should be > 2")
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string


# print(reverse_string('Hello'))


def merge_sorted_list(list1: list, list2: list) -> list:
    """
    Function will merge 2 list and returns sorted list
    :param list1:
    :param list2:
    :return:
    """
    list1_element = list1[0]
    list2_element = list2[0]
    i = 0
    j = 0
    merged_sorted_list = []
    while True:
        list1_element = list1[i] if i < len(list1) else list2[j] if j < len(list2) else None
        list2_element = list2[j] if j < len(list2) else None
        if not (list1_element or list2_element):
            break
        if not list2_element or list1_element < list2_element:
            merged_sorted_list.append(list1_element)
            i += 1
        else:
            merged_sorted_list.append(list2_element)
            j += 1
        print(merged_sorted_list, list1_element, list2_element)
    return merged_sorted_list


print('Result: ', merge_sorted_list([1, 2, 3, 9, 12, 100, 234], [6, 7, 8, 20, 21, 22, 23, 24, 25]))
