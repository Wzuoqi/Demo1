# 创建时间：2021/2/26 22:03
# 1.冒泡排序
def move_max(lst, max_index):
    for i in range(max_index):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]


def pop_sort(lst):
    for i in range(len(lst) - 1, 1, -1):
        move_max(lst, i)


if __name__ == '__main__':
    lst = [1, 9, 6, 7, 8, 3, 4, 5, 2]
    pop_sort(lst)
    print(lst)


# 2.快速排序
# 分为三个步骤：
# 1.从待排序数组中选择一个作为基准值
# 2.移动待排序数组中的元素，以基准值为标准分为两册
# 3.在数组两部分分别重复步骤（需要递归算法）

def partition(lst, start, end):
    """
    用lst[start]作为基准值，在start到end这个范围内分区
    """
    pivot = lst[start]

    while start < end:
        while start < end and lst[end] >= pivot:
            end -= 1
        lst[start] = lst[end]

        while start < end and lst[start] <= pivot:
            start += 1
        lst[end] = lst[start]

    lst[start] = pivot
    return start


def my_quick_sort(lst, start, end):
    if start >= end:
        return

    index = partition(lst, start, end)
    my_quick_sort(lst, start, index - 1)
    my_quick_sort(lst, index + 1, end)


if __name__ == '__main__':
    lst = [4, 3, 2, 8, 1, 5, 7, 2]
    my_quick_sort(lst, 0, len(lst) - 1)
    print(lst)

# 3.希尔排序
# 缩小增量排序
# 每一轮循环 增量/2 相同增量的进行分组

lst = [4, 1, 67, 34, 12, 35, 14, 8, 6, 19]
length = len(lst)
step = length // 2

while step > 0:

    for i in range(step):
        # 插入排序
        for j in range(i + step, length, step):
            if lst[j] < lst[j - step]:
                tmp = lst[j]
                k = j - step

                while k >= 0 and lst[k] > tmp:
                    lst[k + step] = lst[k]
                    k -= step

                lst[k + step] = tmp  # 前面while循环会多减一个step，这里加上
    step //= 2  # 缩小增量
print(lst)


# 4.归并排序

def merge_lst(left_lst, right_lst):
    """两个"""
    res_lst = []
    left_index, right_index = 0, 0
    while left_index < len(left_lst) and right_index < len(right_lst):
        # 将小的放入res_lst中去
        if left_lst[left_index] < right_lst[right_index]:
            res_lst.append(left_lst[left_index])
            left_index += 1
        else:
            res_lst.append(right_lst[right_index])
            right_index += 1

    # 循环结束还有一个元素没放进去
    if left_index == len(left_lst):
        res_lst.extend(right_lst[right_index:])
    else:
        res_lst.extend(left_lst[left_index:])

    return res_lst

