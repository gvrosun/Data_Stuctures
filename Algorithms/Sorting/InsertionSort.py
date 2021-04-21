def swap(data: list, index1: int, index2: int) -> list:
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp
    return data


def insertion_sort(data: list) -> list:
    for i in range(1, len(data) - 1):
        if data[i] > data[i + 1]:
            data = swap(data, i, i+1)
            for j in range(i, -1, -1):
                if data[j+1] < data[j]:
                    data = swap(data, j+1, j)

    return data


print(insertion_sort([3, 2, 6, 66, 4, 1, 8, 0, -3, -5, 7, -10, -11, 9]))
