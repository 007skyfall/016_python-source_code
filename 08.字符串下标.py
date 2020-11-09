name = "helloworld"
# print(name[0], name[1])

# i = 0
# while i <= len(name):
#     print(name[i])
#     i += 1

# 字符串切片操作
"""
语法: name[初识位置:终止位置:步长]
特点: 顾头不顾尾 可以从头开始切, 但是切不到尾部

"""
name1 = name[0:5]
print(name1)
# 从中间指定位置截取
print(name[2:5])
# 从指定位置,切到尾部
print(name[2:])
print("----"*20)
# 负下标
print(name[0:-1])
print("***"*20)
print(name[:5])
print("***"*20)
print(name[:])
print("***"*10)
# name[初识位置:终止位置:步长]
print(name[::2])

# （面试题）给定一个字符串aStr, 请反转字符串
print(name[::-1])
