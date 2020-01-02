# print("nimei")
# name = "app is application"
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name)

# test_name = " ni hao "
# print(test_name.strip())  去除前后端空格
# print(test_name.rstrip()) 去除后面空格
# print(test_name.lstrip()) 去除前面的空格

# str(20) 将数值转换成字符串
# test_birthday = "叫"+str(20)+"声爸爸";
# print(test_birthday)


# print(10/3)
# import this
###########################################################################################
# 列表
# test_list = ["nimei",2]
# -1代表的是最后一个元素  -2返回倒数第二个元素
# print(test_list[-1])

# test_list_1 = ["nimei","jiao","baba"]
# print(test_list_1)
# 修改列表元素
# test_list_1[1] = "niba"
# print(test_list_1)

# test_list_1 = ["nimei", "jiao", "baba"]
# print(test_list_1)
# 给列表添加元素
# test_list_1.append("haha")
# print(test_list_1)

# 在指定位置添加元素
# test_list_1 = ["nimei", "jiao", "baba"]
# test_list_1.insert(1, "ok")
# print(test_list_1)

# 删除指定位置的元素
# test_list_1 = ["nimei", "jiao", "baba"]
# del test_list_1[0]
# print(test_list_1)

# 让元素出栈
# test_list_1 = ["nimei", "jiao", "baba"]
# test_element = test_list_1.pop(0)
# print(test_list_1)
# print(test_element)

# 删除指定元素
# test_list_1 = ["nimei", "jiao", "baba"]
# test_list_1.remove("nimei")
# print(test_list_1)

# 排序
# test_list_1 = ["nimei", "jiao", "baba"]
# test_list_1.sort()
# print(test_list_1)
# 逆序
# test_list_1.sort(reverse=True)
# print(test_list_1)

# 临时排序
# test_list_1 = ["nimei", "jiao", "baba"]
# 临时排序逆序
# test_list_temp = sorted(test_list_1, reverse=True)
# print(test_list_1)
# print(test_list_temp)

# 反转顺序
# test_list_1 = ["nimei", "jiao", "baba"]
# test_list_1.reverse()
# print(test_list_1)

# for 循环
# test_list_1 = ["nimei", "jiao", "baba"]
# for item in test_list_1:
#     print(item)

# 缩进 expected an indented block  应该为缩进块
# Python根据缩进来判断代码行与前一个代码行的关系
# test_list_1 = ["nimei", "jiao", "baba"]
# for item in test_list_1:
# print(item)

# 强行缩进 unexpected indent   意外缩进
# test_list_1 = ["nimei", "jiao", "baba"]
#     print(test_list_1)

# 使用range()函数   包左不包右
# for value in range(1, 5):
#     print(value)

# 使用range()函数创建数字列表
# list_temp = list(range(1, 5))
# print(list_temp)

# 使用range步长 1-10,每次加2
# list_temp = list(range(1, 10, 2))
# print(list_temp)

# 使用range()创建列表，进行计算
# temp = []
# for value in range(1, 5):
#     temp.append(value ** 2)
# print(temp)

# 简洁写法
# temp = [value ** 2 for value in range(1, 5)]
# print(temp)

# 切片 截取列表  这种语法可以让你取到你想取得任何元素子列表
# test_list_1 = ["nimei", "jiao", "baba"]
# print(test_list_1[1:3])
# 从1截取到最后一个
# print(test_list_1[1:])
# 从开头截取到第三个元素
# print(test_list_1[:3])

# 使用切片进行复制    会创建一个新的列表
# test_list_1 = ["nimei", "jiao", "baba"]
# list_temp = test_list_1[:]
# print(list_temp)
# test_list_1.append("haha")
# print(test_list_1)
# print(list_temp)

# 两个数组共享同一块内存，使用同一个内存地址
# test_list_1 = ["nimei", "jiao", "baba"]
# list_temp = test_list_1;
# test_list_1.append("add")
# print(test_list_1)
# print(list_temp)

####################################################################################
# 元祖
# 而不可变的列表被称为元组

# if else
# for value in range(1, 5):
#     if value == 1:
#         print(value)
#     else:
#         print("nimei")

# if elif else
# test_list_1 = ["nimei", "jiao", "baba"]
# for value in test_list_1:
#     if value == 'nimri':
#         print("ok")
#     elif value == "jiao":
#         print("jiao_ok")
#     else:
#         print("haha")

# 判断集合是否为null
# 列表在至少包含一个元素时，返回true
# test_list_1 = ["nimei", "jiao", "baba"]
# if test_list_1:
#     print(test_list_1)
# else:
#     print("null")

alien = {"color": "green", "age": 5, "name": "nimei"}

# 获取键值对
# print(alien["color"])

# 添加键值对
# alien["sex"] = "girl"
# print(alien)

# 修改字典中的值
# alien["sex"] = "boy"
# print(alien)

# 删除字典中的值
# del alien["sex"]
# print(alien)

# 遍历字典
# for key, value in alien.items():
#     print(key)
#     print(value)

# 遍历字典中的所有键  并排序
# print("######################################################")
# for key in sorted(alien.keys()):
#     print(key)
# 遍历字典中的所有值
# for value in alien.values():
#     print(value)

# input 函数
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
# message = input("请输入一个\n数字：")
# 只会输出你输入的数字
# print(message)
# 将字符串转换成数值类型
# message = int(message)
# print(message >= 18)

# 遍历删除指定的元素
# list_test_1 = ["nimei","jiao","baba","nimei"]
#
# while "nimei" in list_test_1:
#     list_test_1.remove("nimei")
# print(list_test_1)

#########################################################################################
# 定义函数
# def get_user():
#     print("nimie")
#
#
# get_user()

# 参数传递
# def get_user(username):
#     print(username)
#
#
# get_user(input())
#
# get_user("nimei")


# 参数默认值   参数有默认值就可以不传递实参
# def get_user(username="haha"):
#     print(username)
#
#
# get_user()

# 参数没有默认值，就必须传递实参
# def get_user(username):
#     print(username)
#
#
# get_user()

# 列表当做参数传递，但是不改变实际列表的值
# function_name(list_name[:])

# 接收任意参数 *username表示：名为username的元祖
# def get_user(*username):
#     print(username)
#
#
# get_user("nimei", "haha")

# 接收任意参数 **username表示：名为username的字典
# def get_user(**username):
#     print(username)
#
#
# get_user(nimei="nimei", haha="haha")

# import 函数调用 导入模块
# import hello
#
# username = hello.get_user("nimei")
# print(username)


# 导入方法
# from hello import get_user as u
# username = u("nimei")
# print(username)


# import sys
#
# print(sys.argv[0])
# # sys.path是python的搜索模块的路径集
# print(sys.path)


#############################################################################################
# 创建类
# 属性的初始值是在 __init__ 函数里赋值的
# import Dog
#
# 导入类  需要这种方式   from dog_test import dog_test
# from dog_test import dog_test
#
# dog = dog_test("nihao", "nihao")
# dog.sit()

# from cat_test import cat_test
#
# cat_test = cat_test("nihao", "nihao")
#
# cat_test.sit()

#############################################################################################




