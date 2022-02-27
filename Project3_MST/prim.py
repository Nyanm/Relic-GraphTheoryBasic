import sys
import numpy as np
MAX = sys.maxsize


class MinHeap(object):
    heap, values = [], []

    def __init__(self, values):
        self.values = values[:]
        self.length = len(values)
        self.heap = list(range(1, len(values) + 1))

    def min_heapify(self, length, index):
        left = 2 * index + 1
        right = left + 1
        if left < length and self.values[self.heap[left]] < self.values[self.heap[index]]:
            cache = left
        else:
            cache = index
        if right < length and self.values[self.heap[right]] < self.values[self.heap[cache]]:
            cache = right
        if cache != index:
            self.heap[cache], self.heap[index] = self.heap[index], self.heap[cache]
            self.min_heapify(length, cache)

    def extract_min(self):
        self.min_heapify(len(self.heap), 0)  # 在取出元素之前维护最小优先队列
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_v = self.heap.pop()  # 弹出最小元素
        return min_v


def extract_min(array):
    if len(array) < 1:
        return -1
    min_heapify(array, len(array), 0)   # 在取出元素之前维护最小优先队列
    array[0], array[-1] = array[-1], array[0]
    min_v = array.pop()   # 弹出最小元素
    return min_v


def min_heapify(array, length, index):   # 最小堆化
    left = 2*index + 1
    right = left + 1
    if left < length and array[left][1] < array[index][1]:
        cache = left
    else:
        cache = index
    if right < length and array[right][1] < array[cache][1]:
        cache = right
    if cache != index:
        array[index], array[cache] = array[cache], array[index]
        min_heapify(array, length, cache)


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix = int(file_data.pop(1)[0])
    file_data.pop(0)
    graph = np.zeros((radix, radix))   # 使用矩阵存储图，方便权值的调用
    for edge in file_data:
        graph[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
        graph[int(edge[1]) - 1][int(edge[0]) - 1] = int(edge[2])
    return graph


def mst_prim(graph, root):
    keys, father, vertexes = [], [], []
    radix, value = len(graph), 0
    for index in range(0, radix):
        keys.append([index + 1, MAX])
        father.append(None)
        vertexes.append(index + 1)
    keys[root - 1][1] = 0
    s_keys = keys[:]   # 使用权值的一个副本来记录权值，在列表keys不断弹出元素时该列表可以方便权值的查找
    for loop in range(0, radix):
        node = extract_min(keys)   # 从最小优先队列中取出最小元素
        vertexes[node[0] - 1] = None
        for index in range(0, radix):   # 遍历当前node连接的所有节点
            vertex = [index + 1, data[node[0] - 1][index]]
            if vertex[1] == 0:   # 节点为空时跳过
                continue
            if vertex[0] in set(vertexes) and data[node[0] - 1][index] < s_keys[vertex[0] - 1][1]:   # 比较权值
                father[vertex[0] - 1] = node[0]   # 更新父节点
                s_keys[vertex[0] - 1][1] = data[node[0] - 1][index]   # 更新s_keys中的权值
                for key in keys:   # 更新keys中的权值
                    if vertex[0] == key[0]:
                        key[1] = data[node[0] - 1][index]
    for key in s_keys:   # 加算总权重
        value += key[1]
    return father, int(value)


def std_output(father, value):
    for index in range(0, len(father)):
        if father[index] is None:
            continue
        print('(', str(index + 1), ',', str(father[index]), ')', sep='')
    print('Weight Sum:', str(value))


filename = input('Please enter the file\'s name:')   # 输入文件名
data = std_input(filename)
result = mst_prim(data, 1)
std_output(result[0], result[1])
