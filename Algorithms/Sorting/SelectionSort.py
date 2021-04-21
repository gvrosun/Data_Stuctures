def swap(data: list, index1: int, index2: int) -> list:
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp
    return data


def selection_sort(data: list) -> list:
    for i in range(0, len(data)):
        small_index = i
        for j in range(i + 1, len(data)):
            if data[small_index] > data[j]:
                small_index = j
        data = swap(data, i, small_index)
        print(data)

    return data


print(selection_sort([3, 2, 6, 66, 4, 1, 8, 0]))
