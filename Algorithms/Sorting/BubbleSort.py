class BubbleSort:
    def __init__(self, data: list):
        self.data = data

    def swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp

    def sort(self):
        index = len(self.data) - 1
        if index < 1:
            return
        i = -1
        while True:
            i += 1
            if i == index:
                i = 0
                index -= 1
            if index == 0:
                return
            if self.data[i] > self.data[i + 1]:
                self.swap(i, i+1)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)


bubble_sort = BubbleSort([3, 7, 10, 6, 2])
bubble_sort.sort()
print(bubble_sort)
