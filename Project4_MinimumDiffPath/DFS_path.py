def get_data(name):  # 读取文件输出图的函数
    with open(name) as file_object:
        data = file_object.readlines()
    length = len(data)
    for index in range(0, length):
        data[index] = data[index].split()
    global head_, tail_  # 使用全局变量向函数外传递首尾
    head_, tail_ = int(data[-2][0]), int(data[-1][0])
    graph = {}  # 创建图
    for index in range(0, int(data[1][0])):  # 初始化图
        graph[index + 1] = []
    for index in range(2, length - 2):  # 填充图
        graph[int(data[index][0])].append(int(data[index][1]))
        graph[int(data[index][1])].append(int(data[index][0]))
    for index in range(0, int(data[1][0])):  # 将图内元素转换为集合以便后续运算
        graph[index + 1] = set(graph[index + 1])
    return graph


def dfs_path(graph, head, tail):  # 主函数
    stack = [(head, [head])]  # 压栈时，将路径一并压入
    while stack:
        (current, path) = stack.pop()
        for vertex in graph[current] - set(path):  # 此时path充当seen，遍历未走过的相邻节点
            if vertex == tail:
                path_list.append(path + [vertex])  # 写入成功的路径
            else:
                stack.append((vertex, path + [vertex]))  # 压入新节点，采用列表组合的方式防止path被修改


def std_output(data_list):  # 转换为规范输出格式
    count = 0
    for index in range(0, len(data_list)):
        for inner_index in range(0, len(data_list[index])):
            print(data_list[index][inner_index], end='')
            try:   # 检查当前元素的后继，若不存在则换行
                data_list[index][inner_index + 1]
            except IndexError:
                print('')
                count += 1
                break
            print('->', end='')
    print('Total paths num:' + str(count))


filename = input('Please enter the file\'s name:')
try:
    text = get_data(filename)
    global path_list
    path_list = []
    dfs_path(text, head_, tail_)
    std_output(path_list)
    del head_, tail_, path_list
except FileNotFoundError:
    print('File not found.')
