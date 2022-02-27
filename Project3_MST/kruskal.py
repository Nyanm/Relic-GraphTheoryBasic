class Union(object):
    leader, size = [0], [0]

    def __init__(self, length):
        self.length = length
        for index in range(1, self.length + 1):
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
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()
    edge_list, node = [], int(file_data.pop(1)[0])
    file_data.pop(0)
    for edge in file_data:
        edge_list.append([int(edge[2]), int(edge[0]), int(edge[1])])
    edge_list.sort(key=lambda x: x[0])   # 对边权进行排序
    return edge_list, node


def mst_kruskal(edge_list, num):
    identity = Union(num)
    father, value = [], 0
    for edge in edge_list:
        if identity.con_check(edge[1], edge[2]):   # 跳过成环边
            pass
        else:   # 非成环边加入边集与总权重
            father.append([edge[1], edge[2]])
            identity.union(edge[1], edge[2])
            value += edge[0]
    return father, value


def std_output(father, value):
    for elem in father:
        print('(', str(elem[0]), ',', str(elem[1]), ')', sep='')
    print('Weight Sum:', str(value))


filename = input('Please enter the file\'s name:')   # 输入文件名
cache = std_input(filename)
result = mst_kruskal(cache[0], cache[1])
std_output(result[0], result[1])
