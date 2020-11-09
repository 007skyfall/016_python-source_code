# break
# name = "chuangkexueyuan"

# for x in name:
#     print("---开始打印")
#
#     print(x)
#
# print("**"*20)
#
# for x in name:
#     print("---开始打印")
#     if x == "u" or x =="a":
#         break
#     print(x)
"""
break :跳出当前所有循环


# contiue

name = "hello world"

for i in name:
    print(i)

print("**"* 20)

for i in name:
    if i == "l":
        continue

    print(i)

"continue : 跳出本次循环"
break 是不可以在判断语句中使用
continue 不可以在判断语句中使用
if a in name:
    print(1)
    continue
"""
name = "hello world"
a = "hello"

i = 0
while i <= 5:
    # 定义变量记录列
    j = 1
    while j <= i:
        print(j,end= "")
        j +=1
        continue
    # 换行
    print(i)
    i += 1


"""
break/continue只能用在循环中，除此以外不能单独使用

break/continue在嵌套循环中，只对最近的一层循环起作用
"""

