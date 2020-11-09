"""
格式:
for 临时变量 in 列表或者字符串或者字典
    执行语句
"""

name = "chuangkexueyuan"

# for i in name:
#     print(i)
sum = 0

for i in name:

    if i == "u" or i == "a":
        sum = sum + 1
print(sum)


for i in name:
    print(i)
else:
    print("已经循环遍历完成")