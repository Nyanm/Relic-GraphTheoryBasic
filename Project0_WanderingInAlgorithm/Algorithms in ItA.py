# ————————————————————————————————归并排序————————————————————————————————
def merge(array_a, array_b):   # 主函数
    sub_array = []
    index_b = index_a = 0
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:
            sub_array.append(array_a[index_a])
            index_a += 1
        else:
            sub_array.append(array_b[index_b])
            index_b += 1

    if index_a == len(array_a):
        for index_c in array_b[index_b:]:
            sub_array.append(index_c)
    else:
        for index_c in array_a[index_a:]:
            sub_array.append(index_c)
    return sub_array


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array)//2
    array_a = merge_sort(array[:middle])
    array_b = merge_sort(array[middle:])
    return merge(array_a, array_b)
# ————————————————————————————————归并排序结束————————————————————————————————


def bubble_sort(array):   # 冒泡排序
    for outside in range(0, len(array)-1):
        for inside in range(0, len(array)-1):
            if array[inside] > array[inside+1]:
                array[inside], array[inside+1] = array[inside+1], array[inside]
    return array


def selection_sort(array):   # 选择排序
    num_index = 0
    result = []
    while len(array) > 0:
        min_num = float("inf")
        for index in range(0, len(array)):
            if array[index] < min_num:
                min_num = array[index]
                num_index = index
        result.append(array.pop(num_index))
    return result


def insert_sort(array):   # 插入排序
    big_num, small_num = float("inf"), float("-inf")
    result = [small_num, big_num]
    for num in array:
        for result_index in range(0, len(result)):
            if result[result_index-1] <= num <= result[result_index]:
                result.insert(result_index, num)
                break
    del result[-1], result[0]
    return result


def quick_sort(array):   # 快速排序 两头双指针缩进，利用元素交换完成划分
    if len(array) < 2:
        return array
    else:
        front, back = 0, len(array) - 1
        benchmark = array[int(len(array)/2)]
        while front != back:
            if array[front] > benchmark:
                array[front], array[back] = array[back], array[front]
            front += 1
            if front == back:
                break
            if array[back] < benchmark:
                array[front], array[back] = array[back], array[front]
            back -= 1
        return quick_sort(array[:int(len(array)/2)]) + quick_sort(array[int(len(array)/2):])


def quick_sort_adv(array):   # 快速排序 Adv 创造新列表来放置划分好的元素，并在返回时合并
    if len(array) < 2:
        return array
    else:
        front, back = [], []
        benchmark = array.pop(0)
        for index in array:
            if index <= benchmark:
                front.append(index)
            else:
                back.append(index)
        return quick_sort_adv(front) + [benchmark] + quick_sort_adv(back)


# ————————————————————————————————快速排序-Lomuto 书中给出的N.Lomuto提出的方法————————————————————————————————
def partition(array, head, tail):   # 对对象进行分类
    benchmark = array[tail]
    index = head - 1
    for global_index in range(head, tail):
        if array[global_index] < benchmark:   # 循环结束后，index指向较小组的最后一个元素
            index += 1
            array[global_index], array[index] = array[index], array[global_index]
    array[tail], array[index+1] = array[index+1], array[tail]
    return index + 1   # 返回主元在列表中的位置


def lomuto(array, head, tail):   # 实际的主函数
    if head < tail:
        checkpoint = partition(array, head, tail)
        lomuto(array, head, checkpoint-1)
        lomuto(array, checkpoint+1, tail)
    return array


def quick_sort_lomuto(array):   # 包装器函数
    return lomuto(array, 0, len(array)-1)
# ————————————————————————————————快速排序 Lomuto 结束————————————————————————————————


# ————————————————————————————————堆排序————————————————————————————————
def max_heapify(array, length, index):   # 传递int(length)表示堆长度而不是len(array)，以此实现对堆的修剪等操作
    left = 2*index + 1
    right = left + 1
    if left < length and array[left] > array[index]:
        cache = left
    else:
        cache = index
    if right < length and array[right] > array[cache]:
        cache = right
    if cache != index:
        array[index], array[cache] = array[cache], array[index]
        max_heapify(array, length, cache)


def build_max_heap(array):   # 构建最大堆
    length = len(array)
    for index in range(length//2 - 1, -1, -1):
        max_heapify(array, length - 1, index)


def heap_sort(array):   # 主函数
    build_max_heap(array)
    for index in range(len(array)-1, -1, -1):
        array[index], array[0] = array[0], array[index]
        max_heapify(array, index, 0)
    return array
# ————————————————————————————————堆排序结束————————————————————————————————


# ————————————————————————————————计数排序————————————————————————————————
def counting(array, sorted_array, key_range):
    cache = []
    for index in range(0, key_range+1):   # 考虑到被排序的列表中可能出现0的情况，作为缓存的列表要多加一个空元素来存放0
        cache.append(0)
    for index in range(0, len(array)):
        cache[array[index]] += 1
    print(cache)
    for index in range(0, key_range+1):
        while cache[index] > 0:
            sorted_array.append(index)
            cache[index] -= 1
    return sorted_array


def counting_sort(array):   # 包装器函数
    sorted_array = []
    key_range = max(array)
    return counting(array, sorted_array, key_range)
# ————————————————————————————————计数排序结束————————————————————————————————


# ————————————————————————————————快速选择————————————————————————————————
def inner_select(array, index, head, tail):
    if head == tail:
        return array[index]
    key = partition(array, head, tail)
    if key+1 == index:
        return array[index]
    elif key+1 > index:
        return inner_select(array, index, head, key-1)
    else:
        return inner_select(array, index, key+1, tail)


def quick_select(array, index):
    tail = len(array)-1
    return inner_select(array, index, 0, tail)
# ————————————————————————————————快速选择结束————————————————————————————————


# ————————————————————————————————备忘自顶向下动态规划————————————————————————————————
# 书中钢条切割问题的带备忘的自顶向下法的实现，value要求输入格式为字典的价格目录，length大小不能超过字典内最大长度
def memoized_cut_rod(value, length):
    memo = [0]
    for index in range(1, length + 1):
        memo.append(-1)
    cut_rod(value, length, memo)
    return memo


def cut_rod(value, notch, memo):
    print(memo)
    if memo[notch] != -1:
        return memo[notch]
    if notch == 0:
        return 0
    cache = -1
    for index in range(1, notch + 1):
        cache = max(cache, value[index] + cut_rod(value, notch - index, memo))
    memo[notch] = cache
    return cache
# ————————————————————————————————备忘自顶向下动态规划结束————————————————————————————————


# ————————————————————————————————自底向上动态规划————————————————————————————————
def bottom_cut_rod(value, length):
    memo = [0]
    for index in range(1, length + 1):
        memo.append(0)
    for index in range(1, length + 1):
        cache = -1
        for inner in range(1, index + 1):
            cache = max(cache, value[inner] + memo[index])
        memo[index] = cache
    return memo
# ————————————————————————————————自底向上动态规划结束————————————————————————————————
