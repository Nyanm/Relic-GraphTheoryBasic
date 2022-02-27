def integer_root(num, index):  # ICPUP 3.1 穷举给定数的n次方根
    ans = 1
    while True:
        power = ans ** index
        if power == num:
            print("yee")
            break
        elif power > num:
            print("boo")
            break
        ans += 1


def root_search(num, precision):  # ICPUP 3.3 二分法查找给定数平方根
    upper, lower = num, 0
    root = (upper + lower) / 2
    while abs(root ** 2 - num) > precision:
        if root ** 2 > num:
            upper = root
            root = (upper + lower) / 2
        else:
            lower = root
            root = (upper + lower) / 2
    return root


def root_newton_method(num, precision):  # ICPUP 3.5 牛顿迭代法（Newton's method）查找给定数平方根
    root = num / 2
    while abs(root ** 2 - num) > precision:
        root = root - (root ** 2 - num) / (2 * root)   # 所用函数为f(x)=x^2-num→0
    return root


def factorial_r(num):   # ICPUP 4.3 阶乘的递归实现
    if num <= 1:
        return num
    else:
        return factorial_r(num-1)


def factorial_i(num):   # ICPUP 4.3 阶乘的迭代实现
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


def fibonacci_sequence(step):   # ICPUP 4.3.1 斐波那契数列
    if step == 0 or step == 1:
        return step
    else:
        return fibonacci_sequence(step-1) + fibonacci_sequence(step-2)


def fibonacci_sequence_(steps):   # ICPUP 4.3.1 斐波那契数列迭代实现
    if steps < 2:
        return steps
    else:
        sequence = [1, 1]
        for step in range(2, steps+1):
            next_step = sequence[-1] + sequence[-2]
            sequence.append(next_step)
        return sequence   # 递归实在是太tm难了


def extreme_divisors(num1, num2):    # ICPUP 5.1 最小公约数与最大公约数
    small, big = 0, 0
    for index in range(2, min(num1, num2)):
        if num1 % index == 0 and num2 % index == 0:
            if small == 0:
                small = index
            big = index
    return [small, big]   # 谁敢反对秘封，就砸烂谁的狗头


def int_to_str(int_num):   # ICPUP 9.3.2 整数转字符串
    if int_num == 0:
        return '0'
    str_num = ''
    int_nums = '0123456789'
    while int_num > 0:
        str_num = int_nums[int_num % 10] + str_num
        int_num = int_num // 10
    return str_num


def binary_search(array, num):   # ICPUP 10.1 二分查找（假设输入的列表为升序数组）
    benchmark = (len(array))//2
    if len(array) == 1:
        return 0
    elif len(array) == 0:   # 列表长度为0即为未找到该数字，跳出错误提示
        raise ValueError('Number not found!')
    elif num == array[benchmark-1]:
        return benchmark - 1
    elif num < array[benchmark-1]:
        return binary_search(array[:benchmark-1], num)
    else:
        return binary_search(array[benchmark:], num) + benchmark


# ————————————————————————————————ICPUP 10.2 归并排序 Cus————————————————————————————————
#     归并排序 Cus 引入了函数变量compare，在默认情况下compare会对输入的两个元素进行正常的比较。同时，用户还可以定义新的compare规则，
# 以此来对更多类型的元素————如字符串进行排序。换言之，这个函数是“可定制的(custom-able)”。
def merge(array_a, array_b, compare):   # 主函数
    sub_array = []
    index_b = index_a = 0
    while index_a < len(array_a) and index_b < len(array_b):
        if compare(array_a[index_a], array_b[index_b]):
            sub_array.append(array_a[index_a])
            index_a += 1
        else:
            sub_array.append(array_b[index_b])
            index_b += 1

    if index_a == len(array_a):
        for remain in array_b[index_b:]:
            sub_array.append(remain)
    else:
        for remain in array_a[index_a:]:
            sub_array.append(remain)
    return sub_array


def merge_sort(array, compare=lambda x, y: x < y):
    if len(array) <= 1:
        return array
    middle = len(array)//2
    array_a = merge_sort(array[:middle], compare)
    array_b = merge_sort(array[middle:], compare)
    return merge(array_a, array_b, compare)
# ————————————————————————————————归并排序 Cus 结束————————————————————————————————
