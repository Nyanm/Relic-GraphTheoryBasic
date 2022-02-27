class Union(object):
    leader, size = [], []

    def __init__(self, length):
        self.length = length
        for index in range(0, self.length):
            self.leader.append(index)
            self.size.append(1)

    def find(self, item):
        while item != self.leader[item]:
            item = self.leader[item]
        return item

    def con_check(self, item_a, item_b):   # 检查两个元素是否属于一个集合
        if self.find(item_a) == self.find(item_b):
            return True
        else:
            return False

    def union(self, item_a, item_b):   # 联合两个集合
        leader_a = self.find(item_a)
        leader_b = self.find(item_b)
        if self.con_check(item_a, item_b):
            pass
        else:
            if self.size[leader_a] > self.size[leader_b]:
                self.leader[leader_b] = leader_a
                self.size[leader_a] += self.size[leader_b]
            else:
                self.leader[leader_a] = leader_b
                self.size[leader_b] += self.size[leader_a]


def std_input(name):
    with open(name) as file_object:
        data = file_object.readlines()
    for index in range(0, len(data)):
        data[index] = data[index].split()
    keys, edges, edge_list = [], [], []
    for index in range(0, int(data[0][0])):
        keys.append(int(data[index * 2 + 1][1]))
        edges.append(data[index * 2 + 2])
    for vertex in range(0, len(keys)):
        for index in edges[vertex]:
            edge_list.append([(keys[vertex] + keys[int(index)]), vertex, int(index)])
            edges[int(index)].remove(str(vertex))   # 删除重复边
    edge_list.sort(key=lambda x: x[0], reverse=True)   # 传出按权重排序好的边列表
    return edge_list, keys


def rescue(name):
    data, vertexes = std_input(name), set()
    print(data)
    edge_list, keys, army = data[0], data[1], 0
    identity = Union(len(keys))
    for edge in edge_list:
        if identity.con_check(edge[1], edge[2]):
            vertexes.add(edge[1])   # 成环边将端点标记
            vertexes.add(edge[2])
        else:
            identity.union(edge[1], edge[2])   # 非成环边加入树
    for vertex in vertexes:   # 计算被标记点的总权重
        army += keys[vertex]
    return army


filename = input('Please enter the file\'s name:')   # 输入文件名
print(rescue(filename))
