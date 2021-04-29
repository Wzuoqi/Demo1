# 创建时间：2021/2/24 20:20
dic = {
    'python': 95,
    'java': 99,
    'c': 100
}

# 1.字典长度
len(dic)

# 2.删除c这个key
del dic['c']

# 3.增加一个key-value对，key值为c，value为100
dic['c'] = 100
print(dic)

# 4.获取所有的key值和value值，存储列表里
lst1 = list(dic.keys())
lst2 = list(dic.values())
print(lst1)
print(lst2)

# 5.获取字典里所有的value的和
sum(dic.values())

# 6.字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
dic1 = {'php': 97}
dic.update(dic1)
print(dic)

# 7.字典应用题：买水果
# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，一共花了89块钱，，小刚购买了葡萄，橘子，樱桃，一共花了87块钱
# 请从上面的描述中提取数据，存储到字典中
info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
}

# 8.集合练习题
lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

set1 = set(lst1)
set2 = set(lst2)

# 哪些整数既在lst1中，也在lst2中（交集）
print(set1.intersection(set2))

# 哪些整数在lst1中，不在lst2中
print(set1.difference(set2))

# 两个列表一共有哪些整数（并集）
print(set1.union(set2))

