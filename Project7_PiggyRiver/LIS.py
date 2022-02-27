def std_input(filename):
    with open(filename) as file_object:
        file_data = file_object.readlines()
    for index in range(len(file_data)):
        file_data[index] = file_data[index].split()
    file_data.pop(0)
    sequence = []
    for data in range(len(file_data)):
        sequence.append([])
        for index in file_data[data]:
            sequence[data].append(int(index))
    return sequence


def lis(queue):

    def search(num, array):
        if len(array) == 1:
            return [0, 1][num > array[0]]
        mid = len(array) // 2
        if num < array[mid]:
            return search(num, array[:mid])
        else:
            return search(num, array[mid:]) + mid

    cache = [queue.pop(0)]
    for index in queue:
        if index > cache[-1]:
            cache.append(index)
        else:
            cache[search(index, cache)] = index

    print(len(cache))


if __name__ == '__main__':
    data = std_input('sample.txt')
    for da in data:
        lis(da)
