import copy


def std_input(filename):
    file, data = open(filename, 'r'), []
    for line in file:
        data.append(line.split())

    size = data.pop(0)
    radix, deg, edges = int(size[0]), int(size[1]), []
    for index in range(deg):
        edge = data.pop(0)
        edges.append([int(edge[2]), int(edge[0]) - 1, int(edge[1]) - 1])
    edges.sort(key=lambda x: x[0])

    path_num = int(data.pop(0)[0])
    paths = []
    for index in range(path_num):
        path = data.pop(0)
        paths.append([int(path[0]) - 1, int(path[1]) - 1])

    return edges, paths, radix


def is_access(graph, path):
    stack, seen = [path[0]], [path[0]]
    while stack:
        temp = stack.pop()
        for node in graph[temp]:
            if node == path[1]:
                return 1
            if node not in set(seen):
                stack.append(node)
                seen.append(node)
    return 0


def slim_path(edges, path, radix):
    l_index = h_index = 0
    low, high, ans = 0, 0, float('inf')
    graph, e_num = [], len(edges)
    for index in range(radix):
        graph.append([])

    def get_graph():
        edge_list, g_graph = edges[l_index: h_index], copy.deepcopy(graph)
        for edge in edge_list:
            g_graph[edge[1]].append(edge[2])
            g_graph[edge[2]].append(edge[1])
        return g_graph

    while not is_access(get_graph(), path):
        if h_index >= e_num:
            return -1
        high = edges[h_index][0]
        h_index += 1

    while True:
        while is_access(get_graph(), path):
            low = edges[l_index][0]
            l_index += 1
        ans = min(ans, high - low)
        while not is_access(get_graph(), path):
            if h_index >= e_num:
                return ans
            high = edges[h_index][0]
            h_index += 1


if __name__ == '__main__':
    file_data = std_input('5.txt')
    for route in file_data[1]:
        print(slim_path(file_data[0], route, file_data[2]))

# 2
# 0
# ----------------------------------------------
# -1
# ----------------------------------------------
# 11
# 10
# ----------------------------------------------
# 2489
# 0
# ----------------------------------------------
# 1006
# 2044
# 1702
# 1935
