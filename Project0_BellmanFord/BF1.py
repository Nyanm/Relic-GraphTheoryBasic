from sys import maxsize
MAX = maxsize


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix, path_data, edge_list = int(file_data.pop(1)[0]), [], []
    file_data.pop(0)
    for edge in file_data:
        if len(edge) == 1:
            path_data.append(int(edge[0]))
            continue
        edge_list.append([int(edge[0]), int(edge[1]), int(edge[2])])
    return radix, edge_list, path_data


def bellman_ford_1(radix, edge_list, path):   # 由于最基础的BF算法是暴力搜索所有边，所以传入的edge_list只是简单的边的集合，没有进行分类
    father, value = [0], [MAX]  # 假定节点编号从1开始
    for index in range(0, radix):
        father.append(None)
        value.append(MAX)
    value[path[0]] = 0

    def relax_(w_edge):
        if value[w_edge[1]] > value[w_edge[0]] + w_edge[2]:
            value[w_edge[1]] = value[w_edge[0]] + w_edge[2]
            father[w_edge[1]] = w_edge[0]

    for loop in range(1, radix):
        for edge in edge_list:
            relax_(edge)

    for edge in edge_list:
        if value[edge[1]] > value[edge[0]] + edge[2]:
            return False

    return father, value[path[1]]


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
    filename = 'sampleEX.txt'
    data = std_input(filename)
    result = bellman_ford_1(data[0], data[1], data[2])
    if result:
        std_output(result[0], result[1], data[2])
    else:
        print('Exist Negative Circle.')
