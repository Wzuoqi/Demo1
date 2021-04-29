# 创建时间：2021/2/25 15:29
# 1.abs函数
def my_abs(number):
    """模拟绝对值函数，返回数字绝对值"""
    if not isinstance(number, (float, int)):
        return number

    if number < 0:
        number *= -1

    return number


# 2.sum函数
def my_sum(lst):
    """模拟求和函数"""
    sum_res = 0
    if not isinstance(lst, list):
        return sum_res

    for item in lst:
        if isinstance(item, (float, int)):
            sum_res += item

    return sum_res


# 3.len函数
# from collections import Iterable
from collections import Iterable


def my_len(obj):
    """获取obj对象的长度"""
    if not isinstance(obj, Iterable):
        # Iterable指一可迭代的对象，如字符串，数组，字典等
        return None
    length = 0
    for x in object:
        length += 1

    return length


# 4.enumerate函数
"""将一个可以遍历的对象组合成一个索引序列"""


def my_enumerate(lst):
    for i in range(len(lst)):
        yield i, lst[i]
        # yield有着和return相似的功能，都会将数据返回给调用者，
        # 不同之处在于，return执行后，函数结束了，而yield执行后，会保留当前的状态，等到下一次执行时，恢复之前的状态，继续执行。


lst = ['a', 'b', 'c']
for index, item in my_enumerate(lst):
    print(index, item)


# 5.any函数
def my_any(list):
    """any函数用于判断迭代参数所有元素中是否至少有一个元素为True"""
    for item in list:
        if item:
            return True
    return False


# 6.bin函数
def my_bin(value):
    """将整数转化为二进制形式"""
    lst = []
    while value:
        if value % 2 == 1:
            lst.append('1')
        else:
            lst.append('0')

        value = value >> 1
        # 左移一位复制给value本身，相当于乘以2
    lst = lst[::-1]
    return ''.join(lst)
print(bin(10))