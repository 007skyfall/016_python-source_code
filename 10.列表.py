"""
列表:
    list = [元素1, 元素2 ]

"""

my_list = ["abc", 123, "def", "ABC"]
print(my_list)
# 下标
# print(my_list[0])
# print(my_list[2])

# 切片[初始位置: 终止位置: 步长]
print(my_list[::2])
print("*"*20)
# 循环遍历
for i in my_list:
    print(i)

# 使用while
i = 0

while i < len(my_list):
    print(my_list[i])
    print(i)
    i += 1