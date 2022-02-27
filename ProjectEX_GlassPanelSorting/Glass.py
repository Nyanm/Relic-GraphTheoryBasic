import PR
import numpy as np


def get_glass(filename):
    file, data = open(filename, 'r'), []
    for line in file:
        data.append(line.split())
    size, num_pos, radix = [], [], int(data.pop(0)[0])
    for index in range(radix):
        size.append([int(data[index][0]), int(data[index][1]), int(data[index][2]), int(data[index][3])])
        num_pos.append([int(data[index + radix][0]), int(data[index + radix][1])])
    return size, num_pos


def get_graph(size, num_pos):
    radix = len(size)
    graph, n_graph, path = [], [], [2 * radix, 2 * radix + 1]
    table = np.zeros((2 * radix + 2, 2 * radix + 2), dtype=int)
    for index in range(radix):
        graph.append([])
        n_graph.append([2 * radix])
        table[2 * radix][index] = 1
    for index in range(radix):
        graph.append([2 * radix + 1])
        n_graph.append([])
        table[index + radix][2 * radix + 1] = 1
    graph.append(list(range(radix)))
    graph.append([])
    n_graph.append([])
    n_graph.append(list(range(radix, 2 * radix)))

    for num in range(radix):
        for glass in range(radix):
            if size[glass][0] < num_pos[num][0] < size[glass][1] and size[glass][2] < num_pos[num][1] < size[glass][3]:
                graph[num].append(glass + radix)
                table[num][glass + radix] = 1
                n_graph[glass + radix].append(num)

    return graph, table, n_graph, path


def get_max_flow(graph, table, n_graph, path):
    flow = PR.push_relabel(graph, table, n_graph, path)
    g_table = flow
    radix = int((len(graph) - 2) / 2)
    n_table = g_table[radix:(2*radix), :radix]
    if radix != sum(sum(n_table)):
        print(-1)
        return
    for index in range(radix):
        for index_ in range(radix):
            if n_table[index][index_]:
                print(index_ + 1, end=' ')


if __name__ == '__main__':
    glass_data = get_glass('sample0.txt')
    graph_data = get_graph(glass_data[0], glass_data[1])
    get_max_flow(graph_data[0], graph_data[1], graph_data[2], graph_data[3])
