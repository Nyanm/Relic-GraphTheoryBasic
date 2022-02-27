class Node(object):
    def __init__(self, data, next_data):
        self.data = data
        self.next_data = next_data

    def __str__(self):   # 打印节点的值
        return str(self.data)

    def get_data(self):   # 获得节点的值
        return self.data

    def get_next(self):   # 获得节点的后继
        return self.next_data

    def set_data(self, new_data):   # 设置节点的值
        self.data = new_data

    def set_next(self, new_next):   # 设置节点的后继
        self.next_data = new_next


class LinkedList(object):
    def __init__(self):
        self.head = Node(None, None)
        self.length = 0

    def is_empty(self):   # 检测是否为空链表
        return self.head is None   # 返回判断结果

    def add(self, value):   # 头插法加入元素
        first_node = Node(value, None)
        first_node.next_data = self.head
        self.head = first_node   # 更新头节点。self.head与first_node均为节点，故直接赋值
        self.length += 1

    def append(self, value):   # 尾接法加入元素
        last_node = Node(value, None)
        if self.is_empty():   # 如为空链表，则直接更新头节点
            self.head = last_node
        else:
            index = self.head
            while index.get_next():   # 遍历链表
                index = index.get_next()
            index.set_next(last_node)   # 将链表尾接入新元素
        self.length += 1

    def search(self, value):   # 按值查找元素，返回元素索引值，如果没有则返回False
        if self.is_empty():
            raise ValueError('List is empty.')   # 链表为空时报错
        else:
            count = 1
            index = self.head
            while index.get_next():
                if index.get_data() == value:
                    return count
                else:
                    count += 1   # 索引自增1，转入下一个元素
                    index = index.get_next()
            return False

    def index_search(self, num):   # 按索引查找元素，返回元素值
        if self.is_empty():
            raise ValueError('List is empty.')
        elif self.length < num < 0:
            raise IndexError('Index out of range.')   # 如检查给定索引超出范围则报错
        else:
            count = 1
            index = self.head
            while count < num:
                index = index.get_next()
                count += 1
            return index.get_data()

    def remove(self, value):   # 按值移除元素，移除成功返回True，未找到返回False
        if self.is_empty():
            raise ValueError('List is empty.')
        else:
            index = self.head
            pre_node = Node(None, None)
            while index.get_next():
                if index.get_data() == value:
                    if not pre_node:
                        self.head = index.get_next
                    else:
                        pre_node.set_next(index.get_next())
                    return True
                pre_node = index
                index = index.get_next()
            return False

    def index_remove(self, num):   # 按索引移除元素
        if self.is_empty():
            raise ValueError('List is empty.')
        elif self.length < num < 0:
            raise IndexError('Index out of range.')  # 如检查给定索引超出范围则报错
        else:
            count = 1
            index = self.head
            pre_node = Node(None, None)
            while count < num:
                count += 1
                pre_node = index
                index = index.get_next()
            if not pre_node:
                self.head = index.get_next
            else:
                pre_node.set_next(index.get_next())

    def insert(self, value, num):   # 按索引插入指定值元素
        if self.is_empty():
            raise ValueError('List is empty.')
        elif num == 1:
            self.add(value)
        elif num > self.length:
            self.append(value)
        elif 1 < num < self.length:
            new_node = Node(value, None)
            count = 1
            index = self.head
            pre_node = Node(None, None)
            while count < num:
                count += 1
                pre_node = index
                index = index.get_next()
            pre_node.set_next(new_node)
            new_node.set_next(index)
