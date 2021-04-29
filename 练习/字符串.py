# 创建时间：2021/2/24 15:42

# 1.将字符串 "abcd" 转成大写
"abcd".upper()

# 2.计算字符串 "cd" 在 字符串 "abcd"中出现的位置
"abcd".find('cd')  # 2

# 3.字符串 "a,b,c,d" ，请用逗号分割字符串，分割后的结果是什么类型的？
"abcd".split(',')

# 4.string = "Python is good", 请将字符串里的Python替换成 python,并输出替换后的结果
string = "Python is good"
string.replace('Python', 'python')

# 5.字符串 string = "python修炼第一期.html"，从这个字符串里获取.html前面的部分，要用尽可能多的方式来做这个事情
string = "python修炼第一期.html"
string[0:string.find('.html')]
string[0:-5]

# 6.获取字符串 string = "Python is good"的长度
string = "Python is good"
print(len(string))

# 7."this is a book", 请用程序判断该字符串是否以this开头
print("this is a book".startswith('this'))

# 8."this is a book", 请用程序判断该字符串是否以apple结尾
"this is a book".endswith('apple')

# 9."this is a book\n"， 字符串的末尾有一个回车符，请将其删除
"this is a book\n".strip()


# 10.实现函数转换字符串大小写
def my_lower(string):
    if not string:
        return None

    lst = list(string)
    for index, item in enumerate(lst):
        ascii_index = ord(item)
        # 获取单个字符的ASCii码
        if 65 <= ascii_index <= 90:
            s = chr(ascii_index + 32)
            lst[index] = s
    return ''.join(lst)


# 11.实现isdigit函数

def my_isdigit(string):
    """判断字符串只包含数字"""
    if not string:
        return False
    for x in string:
        if not (48 <= ord(x) <= 57):
            return False
    return True

# 12.实现字符串count方法

def my_count(source, target, start, end):
    """查找target在source区间中出现的次数"""
    if not source or not target:
        return 0
    if start>=len(source) or start<0:
        return 0
    # 验证合法性

    count = 0
    if end > len(source):
        end = len(source)

    index = start
    while index < end:
        t_index = 0
        while t_index < len(target) and t_index+len(target) <= end:
            if target[t_index] != source[index+t_index]:
                break
            t_index += 1

            if t_index == len(target):
                index += len(target)
                count += 1
            else:
                index += 1
    return count