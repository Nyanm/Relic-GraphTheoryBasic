import numpy as np
import sys

MAX = sys.maxsize


def std_input(filename):
    with open(filename) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix = int(file_data.pop(0)[0])
    graph, des, max_num = [], [], 0
    table = np.zeros((radix, radix))
    for index in range(radix):
        graph.append([])

    for edge in file_data:
        if len(edge) == 1:
            continue
        if len(edge) == 2:
            des = [int(edge[0]) - 1, int(edge[1]) - 1]
            continue
        graph[int(edge[0]) - 1].append(int(edge[1]) - 1)
        table[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
        max_num = max(max_num, int(edge[2]))

    return graph, table, des, [radix, max_num]


def ff_cs(graph, table, des, graph_data):
    max_flow, scale = 0, graph_data[1] // 2
    head, tail, radix = des[0], des[1], graph_data[0]

    g_graph = graph[:]
    g_table = np.tile(table, 1)

    def get_graph():
        p_table = np.tile(g_table, 1)

        for vertex in range(radix):
            for p_node in g_graph[vertex]:
                if p_table[vertex][p_node] < scale:
                    p_table[vertex][p_node] = 0
        return p_table

    def find_path():
        p_table = get_graph()
        stack = [(head, [head], MAX)]
        while stack:
            (current, seen, capacity) = stack.pop()
            for node in g_graph[current]:
                if node in set(seen) or p_table[current][node] == 0:
                    continue
                if node == tail:
                    return seen + [node], min(capacity, p_table[current][node])
                else:
                    stack.append((node, seen + [node], min(capacity, p_table[current][node])))
        return False

    while scale >= 1:
        while True:
            path_data = find_path()
            try:
                path, flow = path_data[0], path_data[1]
            except TypeError:
                break
            max_flow += flow
            for index in range(0, len(path) - 1):
                g_table[path[index]][path[index + 1]] -= flow
                if g_table[path[index + 1]][path[index]] == 0:
                    g_graph[path[index + 1]].append(path[index])
                g_table[path[index + 1]][path[index]] += flow

        scale = scale // 2
    print(max_flow)


if __name__ == '__main__':
    data = std_input('test-3.txt')
    ff_cs(data[0], data[1], data[2], data[3])
