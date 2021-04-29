# 创建时间：2021/2/24 22:29

# 使用input函数接收用户的输入，如果用户输入的整数是偶数，则
# 使用print函数输出"你输入的整数是:{value}, 它是偶数", {value}部分要替换成用户的输入。
value = input("请输入一个整数：")
float_value = float(value)
int_value = int(float_value)
if int_value == float_value:
    if int_value % 2 == 0:
        print(f"你输入的整数是：{value}，它是偶数")
    else:
        print(f"你输入的整数是：{value}，它是奇数")
else:
    print("它不是一个整数")


