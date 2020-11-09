"""
    *
    * *
    * * *
    * * * *
    * * * * *

"""
# 定义一个变量,记录行数
# i = 0
# while i <= 5:
#     print("*")
#     i +=1

# 定义一个变量, 记录列数
# j = 1
# while j <= 5:
#     print("*", end=" ")
#     j += 1


# 建立行列关系
# # 定义变量记录行数
# i = 0
# while i <= 5:
#     # 定义变量记录列
#     j = 1
#     while j <= i:
#         print("* ",end= "")
#         j +=1
#     # 换行
#     print()
#     i += 1

i = 1
while i<= 12:
    j=1
    while j<=i:
        print("%d*%d=%-2d " % (j, i, i*j), end = '')
        j+=1
    print('\n')
    i+=1