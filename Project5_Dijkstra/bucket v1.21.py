from sys import maxsize
import numpy as np

MAX = maxsize


class Bucket(object):
    bucket = []

    def __init__(self, size):
        for index in range(0, size):
            self.bucket.append([])
        self.index = 0

    def update(self, node, value):
        self.bucket[value].append(node)

    def find_min(self):
        while len(self.bucket[self.index]) == 0:
            self.index += 1
        cache = self.bucket[self.index]
        self.index += 1
        return cache


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix, path_data, edge_list, max_data = int(file_data.pop(1)[0]), [], [], 0
    for index in range(0, radix + 1):
        edge_list.append([])
    file_data.pop(0)
    for edge in file_data:
        if len(edge) == 1:
            path_data.append(int(edge[0]))
            continue
        edge_list[int(edge[0])].append([int(edge[1]), int(edge[2])])
        max_data = max(max_data, int(edge[2]))
    return edge_list, (radix, path_data, max_data)


def dijkstra_bucket(edge_list, others):
    radix, path, max_data = others[0], others[1], others[2]
    bucket = Bucket(max_data * radix + 1)
    father, vertexes, value = [None] * (radix + 1), list(range(1, radix + 1)), [MAX] * (radix + 1)
    bucket.update(path[0], 0)
    value[path[0]] = 0

    while vertexes:
        nodes = bucket.find_min()[:]
        for node in nodes:
            try:
                vertexes.remove(node)
            except ValueError:
                pass
            for edge in edge_list[node]:
                if edge[0] in set(vertexes):
                    if value[edge[0]] > value[node] + edge[1]:
                        value[edge[0]] = value[node] + edge[1]
                        father[edge[0]] = node
                        bucket.update(edge[0], int(value[edge[0]]))
            if node == path[1]:
                return father, value[node]


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
    result = dijkstra_bucket(data[0], data[1])
    std_output(result[0], result[1], data[1][1])
