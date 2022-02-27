from sys import maxsize

MAX = maxsize


def std_input(name):
    with open(name) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    radix, path_data, edge_list = int(file_data.pop(1)[0]), [], []
    for index in range(0, radix + 1):
        edge_list.append([])
    file_data.pop(0)
    for edge in file_data:
        if len(edge) == 1:
            path_data.append(int(edge[0]))
            continue
        edge_list[int(edge[0])].append([int(edge[1]), int(edge[2])])
    return edge_list, (radix, path_data)


def bellman_ford_2(edge_list, others):
    radix, path = others[0], others[1]
    father, value, queue = [0], [MAX], []  # 假定节点编号从1开始
    for index in range(0, radix):
        father.append(None)
        value.append(MAX)
    value[path[0]] = 0
    queue.append(path[0])

    while queue:
        node = queue.pop()
        for edge in edge_list[node]:
            if value[edge[0]] > value[node] + edge[1]:
                value[edge[0]] = value[node] + edge[1]
                father[edge[0]] = node
                queue.append(edge[0])

    for node in range(1, radix + 1):
        for edge in edge_list[node]:
            if value[edge[0]] > value[node] + edge[1]:
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
    result = bellman_ford_2(data[0], data[1])
    if result:
        std_output(result[0], result[1], data[1][1])
    else:
        print('Exist Negative Circle.')
