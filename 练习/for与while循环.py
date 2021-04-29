# 创建时间：2021/2/24 23:20
# 1.用for循环遍历字典
# 方法一
dic = {
    'python': 90,
    'java': 95
}

for key in dic:
    print(key, dic[key])
# 方法二
dic = {
    'python': 90,
    'java': 95
}

for key,value in dic.items():
    print(key, value)

# 2.寻找列表中的最大值
lst = [3, 6, 1, 8, 1, 9, 2]
max_item = lst[0]
for item in lst:
    if item > max_item:
        max_item = item
print(max_item)

# 3.寻找组合
lst1 = [3, 6, 1, 8, 1, 9, 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]
max_x0 = 0

for x1 in lst1:
    for x2 in lst2:
        x0 = x1*x2
        if x0 > max_x0:
            max_x0 = x0
        if x1 + x2 == 10:
            print((x1, x2))
print(max_x0)

# 4.break与continue
# 使用input函数接受用户的输入，如果用户输入的数值小于等于10，则判断是奇数还是偶数，如果数值大
# 于10，则输出“输入大于10，不判断奇偶”,用户输入quit，结束程序
while True:
    input_str = input("请输入一个正整数,如果想停止程序，输入quit:")
    if input_str == 'quit':
        break
    number = int(input_str)
    if number > 10:
        continue
    # 如果number大于10那么跳过接下来四行代码
    if number % 2 == 0:
        print("输入为偶数")
    else:
        print("输入为奇数")
