from sys import maxsize

MAX = maxsize


class MinHeap(object):


    def __init__(self, radix, root):
        self.values, self.heap = [MAX], [0]
        for index in range(1, radix + 1):
            self.values.append(MAX)
            self.heap.append(index)
        self.length = len(self.heap)
        self.values[root] = 0

    def min_heapify(self, index):
        left = 2 * index + 1
        right = left + 1
        if left < self.length and self.values[self.heap[left]] < self.values[self.heap[index]]:
            cache = left
        else:
            cache = index
        if right < self.length and self.values[self.heap[right]] < self.values[self.heap[cache]]:
            cache = right
        if cache != index:
            self.heap[cache], self.heap[index] = self.heap[index], self.heap[cache]
            self.min_heapify(cache)

    def extract_min(self):
        if len(self.heap) == 0:
            return -1
        for index in range(self.length // 2, -1, -1):
            self.min_heapify(index)  # 在取出元素之前维护最小优先队列
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_v = self.heap.pop()  # 弹出最小元素
        self.length = len(self.heap)
        return min_v


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix, path_data, edge_list = int(file_data.pop(1)[0]), [], []
    for index in range(0, radix + 1):
        edge_list.append([])
    file_data.pop(0)
    for edge in file_data:
        if len(edge) == 1:
            path_data.append(int(edge[0]))
            continue
        edge_list[int(edge[0])].append([int(edge[1]), int(edge[2])])
    return edge_list, (radix, path_data)


def dijkstra_heap(edge_list, others):
    radix, path = others[0], others[1]
    heap = MinHeap(radix, path[0])
    father, vertexes = [None] * (radix + 1), list(range(1, radix + 1))

    while vertexes:
        node = heap.extract_min()
        vertexes.remove(node)
        for edge in edge_list[node]:
            if edge[0] in set(vertexes):
                if heap.values[edge[0]] > heap.values[node] + edge[1]:
                    heap.values[edge[0]] = heap.values[node] + edge[1]
                    father[edge[0]] = node
        if node == path[1]:
            break

    return father, heap.values[node]


def std_output(father, value, path_data):
    current, path = path_data[1], []
    while current:
        path.append(current)
        current = father[current]
    path.reverse()
    for index in range(0, len(path)):
        print(path[index], end='')
        try:
            test = path[index + 1]
            print('->', end='')
        except IndexError:
            print()
    print('Total Value:', int(value))


if __name__ == '__main__':
    filename = 'test-3.txt'
    data = std_input(filename)
    result = dijkstra_heap(data[0], data[1])
    std_output(result[0], result[1], data[1][1])
