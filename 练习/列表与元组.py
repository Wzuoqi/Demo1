# 创建时间：2021/2/24 16:21
lst = [1, 2, 3, 4, 5]
# 1.求列表长度
len(lst)

# 2.判断6是否在列表中
print(6 in lst)

# 3.lst + [6, 7, 8] 的结果是什么？
print(lst + [6, 7, 8])

# 4.lst*2的结果是什么？
print(lst * 2)

# 5.列表里元素的最大值是多少
max(lst)

# 6.列表里元素的最小值是多少
min(lst)

# 7.列表里所有元素的和是多少
sum(lst)

# 8.在索引1的后面新增一个的元素10
lst.insert(1, 10)

# 9.在列表的末尾新增一个元素20
lst.append(20)

# 10.lst = [1, [4, 6], True] 请将列表里所有数字修改成原来的两倍
# 方法一：逐个更改
lst = [1, [4, 6], True]
lst[0] = 2
lst[1][0] = 4
lst[1][1] = 6


# 方法二：定义函数
def double_list(lst):
    """将列表中的数据全部翻倍，不管嵌套几层list"""
    for index, item in enumerate(lst):
        # enumerate函数将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
        if isinstance(item, bool):
            # isinstance函数来判断对象的数据类型
            continue
        if isinstance(item, (int, float)):
            lst[index] *= 2
        if isinstance(item, list):
            double_list(item)
    return lst


if __name__ == '__main__':
    lst = [1, [4, 6], True]
    print(double_list(lst))

# 11.合并列表和字符串
lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst.extend(lst2)
str1 = "1,2,3"
str2 = "4,5,6"
str1 += str2

# 12.列表排序
lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
lst.sort()  # 从小到大
lst.sort(reverse=True)  # 从大到小
lst2 = lst[::-1]  # 翻转列表里的所有元素
