import numpy as np
from sys import maxsize
MAX = maxsize


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
        current = left
    else:
        current = index
    if right < length and array[right][1] < array[current][1]:
        current = right
    if current != index:
        array[index], array[current] = array[current], array[index]
        min_heapify(array, length, current)


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix, path_data = int(file_data.pop(1)[0]), []
    file_data.pop(0)
    graph = np.zeros((radix, radix))   # 使用矩阵存储图，方便权值的调用
    for edge in file_data:
        if len(edge) == 1:
            path_data.append(int(edge[0]))
            continue
        graph[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
    return graph, path_data


def dijkstra_heap(graph, path_data):
    radix = len(graph)
    father, value_st, value_dy, vertexes, tol_value = [], [], [], [], 0
    for index in range(1, radix + 1):
        father.append(None)
        value_st.append(MAX)
        value_dy.append([index, MAX])
        vertexes.append(index)
    value_st[path_data[0] - 1] = 0
    value_dy[path_data[0] - 1][1] = 0

    def relax(u, v):
        if value_st[v - 1] > value_st[u - 1] + graph[u - 1][v - 1]:
            value_st[v - 1] = value_st[u - 1] + graph[u - 1][v - 1]
            for value in value_dy:
                if value[0] == v:
                    value[1] = value_st[v - 1]
                    break
            father[v - 1] = u

    for loop in range(0, radix):
        node = extract_min(value_dy)
        vertexes[node[0] - 1] = None
        for index in range(1, radix + 1):  # 遍历当前node连接的所有节点
            vertex = [index, graph[node[0] - 1][index - 1]]
            if vertex[1] == 0:
                continue
            if vertex[0] in set(vertexes):
                relax(node[0], vertex[0])
        if vertexes[path_data[1] - 1] is None:
            break

    return father, value_st


def std_output(father, value, path_data):
    current, path = path_data[1], []
    while current:
        path.append(current)
        current = father[current - 1]
    for index in range(0, len(path)):
        print(path[index], end='')
        try:
            test = path[index + 1]
            print('->', end='')
        except IndexError:
            print()
    print('Total Value:', value[path_data[1] - 1])


if __name__ == '__main__':
    filename = input('Please enter the file\'s name:')  # 输入文件名
    cache = std_input(filename)
    result = dijkstra_heap(cache[0], cache[1])
    std_output(result[0], result[1], cache[1])

"""
test data
13
8
1 5 1
1 2 12
1 4 16
2 6 17
2 3 16
4 3 6
5 6 2
5 7 15
6 8 3
7 8 4
7 4 5
8 7 4
8 3 18
1
3
"""