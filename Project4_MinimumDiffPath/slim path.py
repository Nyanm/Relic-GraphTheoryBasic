# 小節線を飛び越せ―!!
import numpy as np
from sys import maxsize
MAX = maxsize


class MinHeap(object):

    def __init__(self, radix, edge):
        self.values, self.heap, self.sign = [MAX], [0], [True]
        for index in range(1, radix + 1):
            self.values.append(MAX)
            self.heap.append(index)
            self.sign.append(True)
        self.length = len(self.heap)
        self.values[edge[0]] = self.values[edge[1]] = 0

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
    radix, path_data = int(file_data.pop(0)[0]), []
    graph = np.zeros((radix, radix))   # 使用矩阵存储图，方便权值的调用
    for edge in file_data:
        if len(edge) == 1:
            continue
        if len(edge) == 2:
            path_data.append([int(edge[0]), int(edge[1])])
            continue
        graph[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
        graph[int(edge[1]) - 1][int(edge[0]) - 1] = int(edge[2])
    return graph, path_data


def slim_path(graph, path_data):
    if graph[path_data[0] - 1][path_data[1] - 1] != 0:
        return 0

    def get_num(node):
        num = 0
        for vertex in graph[node - 1]:
            if vertex == 0:
                continue
            num += 1
        return num

    def dijkstra(edge):
        max_temp = min_temp = graph[edge[0] - 1, edge[1] - 1]
        heap = MinHeap(radix, edge)
        vertexes = list(range(1, radix + 1))

        def relax(u, v):
            if max_temp >= graph[u - 1][v - 1] >= min_temp:
                cache = 0
                bool_cache = True
            elif graph[u - 1][v - 1] > max_temp:
                cache = graph[u - 1][v - 1] - max_temp
                bool_cache = True
            else:
                cache = min_temp - graph[u - 1][v - 1]
                bool_cache = False
            if heap.values[v]:
                pass

        while vertexes:
            node = heap.extract_min()
            print(node, vertexes)
            vertexes.remove(node)
            if heap.sign[node]:
                max_temp += heap.values[node]
            else:
                min_temp -= heap.values[node]

            for index in range(1, radix + 1):
                if graph[node - 1][index - 1] == 0:  # 节点为空时跳过
                    continue
                if index in set(vertexes):
                    relax(node, index)
            if node == goal:
                break

        print(max_temp, min_temp)
        return max_temp - min_temp

    radix, ans = len(graph), MAX
    if get_num(path_data[0]) > get_num(path_data[1]):
        goal, root = path_data[0], path_data[1]
    else:
        goal, root = path_data[1], path_data[0]

    for fewer in range(1, radix + 1):
        if graph[root - 1][fewer - 1] == 0:
            continue
        result = dijkstra([root, fewer])
        ans = min(ans, result)

    return int(ans)


if __name__ == '__main__':

    filename = 'data'
    data = std_input(filename)
    for path in data[1]:
        print(slim_path(data[0], path))


# ————————————抱憾而终——————————————
