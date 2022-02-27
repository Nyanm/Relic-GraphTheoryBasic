import numpy as np
import sys

MAX = sys.maxsize


class ExcessBucket(object):
    def __init__(self, radix):
        self.bucket = []
        self.height = [0] * radix
        self.excess = [0] * radix
        self.index = radix * 2 - 1
        for index in range(radix * 2):
            self.bucket.append([])

    def find_max(self):
        while not self.bucket[self.index]:
            self.index -= 1
        if self.index <= 0:
            return -1
        for vertex in self.bucket[self.index]:
            if self.excess[vertex] <= 0:
                continue
            else:
                return vertex
        self.index -= 1
        return self.find_max()

    def relabel(self, vertex):
        self.index += 1
        self.bucket[self.index].append(vertex)
        self.height[vertex] += 1

    def is_pushable(self, vertex, node):
        return self.height[vertex] == self.height[node] + 1


def std_input(filename):
    with open(filename) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()

    # 由于需要反向BFS，所以特别设立了一个反向图用于搜索
    radix, graph, n_graph, des = int(file_data.pop(0)[0]), [], [], [int(file_data.pop(0)[0]), 0]
    table = np.zeros((radix, radix))
    for index in range(radix):
        graph.append([])
        n_graph.append([])

    for edge in file_data:
        if len(edge) == 2:
            des[0] = int(edge[0]) - 1
            des[1] = int(edge[1]) - 1
            continue
        graph[int(edge[0]) - 1].append(int(edge[1]) - 1)
        n_graph[int(edge[1]) - 1].append(int(edge[0]) - 1)
        table[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])

    return graph, table, n_graph, des


def push_relabel(graph, table, n_graph, path):
    # 初始化数据，包括高度函数、反向BFS
    radix, level = len(graph), 0
    head, tail = path[0], path[1]
    excess = ExcessBucket(radix)
    queue, seen = [[tail]], [tail, head]
    g_table = np.tile(table, 1)

    # 反向BFS设定高度
    while queue[0]:
        vertexes = queue.pop()
        queue.append([])
        for vertex in vertexes:
            excess.bucket[level].append(vertex)
            excess.height[vertex] = level
            for node in n_graph[vertex]:
                if node in set(seen):
                    continue
                else:
                    queue[0].append(node)
                    seen.append(node)
        level += 1
    excess.height[head] = radix - 1
    excess.excess[head] = MAX

    # Push函数，实现饱和/非饱和推送并更新剩余网络
    def push(sou, des):
        if excess.excess[sou] >= g_table[sou][des]:
            flow = g_table[sou][des]
        else:
            flow = excess.excess[sou]

        excess.excess[sou] -= flow
        g_table[sou][des] -= flow
        if g_table[des][sou] == 0:
            graph[des].append(sou)
        excess.excess[des] += flow
        g_table[des][sou] += flow

    # 在起点饱和推送
    for node in graph[head]:
        push(head, node)
    excess.excess[head] = 0

    # Push-Relabel过程
    while True:
        vertex = excess.find_max()
        if vertex == -1:
            break
        access = []
        for node in graph[vertex]:
            if g_table[vertex][node] == 0:
                continue
            if excess.is_pushable(vertex, node):
                push(vertex, node)
                access.append(node)
        if not access:
            excess.relabel(vertex)

    # 终点出边割差即为最小割，即最大流
    # print("Max Flow =", sum(g_table[tail]) - sum(table[tail]))
    return g_table


if __name__ == '__main__':
    data = std_input('test-2.txt')
    push_relabel(data[0], data[1], data[2], data[3])
