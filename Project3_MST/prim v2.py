import sys
import numpy as np

MAX = sys.maxsize


class MinHeap(object):
    values, heap = [MAX], [0]

    def __init__(self, radix, root):
        for index in range(1, radix + 1):
            self.values.append(MAX)
            self.heap.append(index)
        self.length = len(self.heap)
        self.values[root] = 0
        print(self.heap, self.values)

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
        for index in range(self.length//2, -1, -1):
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
    radix = int(file_data.pop(1)[0])
    file_data.pop(0)
    graph = np.zeros((radix, radix))  # 使用矩阵存储图，方便权值的调用
    for edge in file_data:
        graph[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
        graph[int(edge[1]) - 1][int(edge[0]) - 1] = int(edge[2])
    return graph


def mst_prim(graph, root):
    father, vertexes = [None], []
    radix, value = len(graph), 0
    for index in range(0, radix):
        father.append(None)
        vertexes.append(index + 1)
    values = MinHeap(radix, root)

    while vertexes:
        node = values.extract_min()  # 从最小优先队列中取出最小元素
        vertexes.remove(node)
        for index in range(1, radix + 1):  # 遍历当前node连接的所有节点
            if graph[node - 1][index - 1] == 0:  # 节点为空时跳过
                continue
            if index in set(vertexes) and graph[node - 1][index - 1] < values.values[index]:  # 比较权值
                father[index] = node  # 更新父节点
                values.values[index] = graph[node - 1][index - 1]  # 更新s_keys中的权值
    values.values.pop(0)
    return father, values.values


def std_output(father, values):
    for index in range(0, len(father)):
        if father[index] is None:
            continue
        print('(', str(index), ',', str(father[index]), ')', sep='')
    tol_value = 0
    for value in values:
        tol_value += value
    print('Total Weight:', int(tol_value))


"""filename = input('Please enter the file\'s name:')  # 输入文件名"""
data = std_input('test-1.txt')
result = mst_prim(data, 1)
std_output(result[0], result[1])
