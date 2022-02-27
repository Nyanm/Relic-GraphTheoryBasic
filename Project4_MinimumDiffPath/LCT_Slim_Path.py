import sys


class LCT(object):
    def __init__(self, radix):
        # Define "Node 0" as a nil node.
        self.ch, self.fa, self.rev, self.root = [[None, None]], [None], [False], [True]
        for index in range(radix):
            self.ch.append([0, 0])
            self.fa.append(0)
            self.rev.append(False)
            self.root.append(True)

    def which_child(self, node):
        return self.ch[self.fa[node]][1] is node

    def push_reverse(self, node):
        if not node:
            return
        self.ch[node][0], self.ch[node][1] = self.ch[node][1], self.ch[node][0]
        self.rev[node] ^= True

    def push_down(self, node):  # 亲爱的你node塌了
        if self.rev[node]:
            self.push_reverse(self.ch[node][0])
            self.push_reverse(self.ch[node][1])
            self.rev[node] = False

    def rotate(self, node):
        print(self.fa)
        if self.root[node]:
            return
        father = self.fa[node]
        grandfather = self.fa[father]
        ch_id = self.which_child(node)
        self.ch[father][ch_id] = self.ch[node][ch_id ^ 1]
        if not self.ch[node][ch_id ^ 1]:
            self.fa[self.ch[node][ch_id ^ 1]] = father
        self.ch[node][ch_id ^ 1] = father
        self.fa[father] = node
        self.fa[node] = grandfather
        self.fa[0] = None
        if not self.root[father]:
            self.ch[grandfather][father == self.ch[grandfather][1]] = node
        else:
            self.root[node], self.root[father] = True, False
        print(self.fa)

    def push(self, node):
        if not self.root[node]:
            self.push(self.fa[node])
        self.push_down(node)

    def splay(self, node):
        self.push(node)
        father = self.fa[node]
        while not self.root[node]:
            if not self.root[father]:
                if self.which_child(node) == self.which_child(father):
                    self.rotate(father)
                else:
                    self.rotate(node)
            self.rotate(node)

    def access(self, node):
        temp, node_ = 0, node
        while True:
            self.splay(node_)
            self.root[self.ch[node_][1]] = True
            self.root[temp] = False
            self.ch[node_][1] = temp
            temp = node_
            node_ = self.fa[node_]
            if not node_:
                break

    def make_root(self, node):
        print("access", node)
        self.access(node)
        print("splay", node)
        self.splay(node)
        self.push_reverse(node)

    def cut(self, edge):
        u, v = edge[1], edge[2]
        self.make_root(u)
        self.access(v)
        self.splay(v)
        self.fa[u] = self.ch[v][0] = 0

    def link(self, edge):
        u, v = edge[1], edge[2]
        self.make_root(u)
        self.fa[u] = v

    def is_connect(self, head, tail):
        head_, tail_ = head, tail
        while self.fa[head_]:
            head_ = self.fa[head_]
        while self.fa[tail_]:
            tail_ = self.fa[tail_]
        return head_ == tail_


def std_input(filename):
    with open(filename) as file_object:
        data = file_object.readlines()
    for index in range(0, len(data)):
        data[index] = data[index].split()

    size = data.pop(0)
    radix, deg, edges = int(size[0]), int(size[1]), []
    for index in range(deg):
        edge = data.pop(0)
        edges.append([int(edge[2]), int(edge[0]), int(edge[1])])
    edges.sort(key=lambda x: x[0])

    path_num = int(data.pop(0)[0])
    paths = []
    for index in range(path_num):
        path = data.pop(0)
        paths.append([int(path[0]), int(path[1])])

    return edges, paths, radix


def slim_path(edges, pole, radix):
    head, tail = pole[0], pole[1]
    l_index, h_index, e_num = 0, 0, len(edges)
    lct = LCT(radix)
    print(edges)
    print(pole)

    while not lct.is_connect(head, tail):
        edge = edges[h_index]
        print(edge)
        lct.link(edge)
        h_index += 1
        print("pass", lct.fa)

    high, low, ans = edges[h_index][0], 0, sys.maxsize
    while True:
        while lct.is_connect(head, tail):
            lct.cut(edges[l_index])
            low = edges[l_index][0]
            l_index += 1
        ans = min(ans, high - low)
        while not lct.is_connect(head, tail):
            if h_index >= e_num:
                return ans
            lct.link(edges[h_index])
            high = edges[h_index][0]
            h_index += 1


if __name__ == '__main__':
    file_data = std_input('1.txt')
    for path_ in file_data[1]:
        slim_path(file_data[0], path_, file_data[2])
