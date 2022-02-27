from sys import maxsize

MAX = maxsize


class Union(object):

    def __init__(self, length):
        self.leader, self.size = [0], [0]
        self.length = length
        for index in range(1, self.length + 1):
            self.leader.append(index)
            self.size.append(1)

    def find(self, item):
        while item != self.leader[item]:
            item = self.leader[item]
        return item

    def con_check(self, item_a, item_b):  # 检查两个元素是否属于一个集合
        if self.find(item_a) == self.find(item_b):
            return True
        else:
            return False

    def union(self, item_a, item_b):  # 联合两个集合
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
    radix, edge_list, path_data = int(file_data.pop(0)[0]), [], []
    for edge in file_data:
        if len(edge) == 1:
            continue
        if len(edge) == 2:
            path_data.append([int(edge[0]), int(edge[1])])
            continue
        edge_list.append([int(edge[2]), int(edge[0]), int(edge[1])])

    edge_list.sort(key=lambda x: x[0])
    return edge_list, path_data, radix


def kruskal(edge_list, radix, path):
    tree = []
    for index in range(0, radix + 1):
        tree.append([])
    identity = Union(radix)
    for edge in edge_list:
        if identity.con_check(edge[1], edge[2]):  # 跳过成环边
            pass
        else:  # 非成环边加入边集与总权重
            tree[edge[1]].append([edge[2], edge[0]])
            tree[edge[2]].append([edge[1], edge[0]])
            identity.union(edge[1], edge[2])
        if identity.con_check(path[0], path[1]):
            return dfs(tree, path)
    return MAX


def dfs(tree, path):
    high = low = False
    stack = [(path[0], [path[0]], high, low)]
    while stack:
        (current, seen, high, low) = stack.pop()
        for vertex in tree[current]:
            if vertex[0] in set(seen):
                continue
            if high is False:
                high = low = vertex[1]
            else:
                if vertex[1] > high:
                    high = vertex[1]
                elif vertex[1] < low:
                    low = vertex[1]
            if vertex[0] == path[1]:
                return high - low
            else:
                stack.append((vertex[0], seen + [vertex[0]], high, low))


def slim_path(edge_list, path_data, radix):
    for path in path_data:
        ans, edge_list_, count = MAX, edge_list[:], 0
        while edge_list_:
            ans = min(ans, kruskal(edge_list_, radix, path))
            if count == 0 and ans == MAX:
                ans = -1
                break
            count += 1
            edge_list_.pop(0)
        print(ans)


if __name__ == '__main__':
    data = std_input('5.txt')
    slim_path(data[0], data[1], data[2])
