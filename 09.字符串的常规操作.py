my_str = "hell11111oworlItcasaniTcastcpp"

# find
"""
查找字符串存不存在另一个字符串中, 如果存在, 则返回字符开始的下标,
如果不存在,则返回 -1
# mystr.find(str, )
index = my_str.find("y", 0 , len(my_str))

print(index)
快速查看函数
ctrl  +点击左键
"""
# mystr.find(str, )

# index
"""
作用: 同find 如果存在则返回下标, 如果不存在, 则会报错

index = my_str.index("hello", 5, len(my_str))
print(index)
print(123456)
"""

#count
"""
作用: 查看字符在另一个字符串中出现的次数
返回值: 出现的次数
count = my_str.count("a")
print(count)

"""
# replace
"""
作用:把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
返回值: 字符串
str3 = my_str.replace("ll", "o")
print(str3)
a =1
b =2
a , b = b ,a
print(b)

"""

# split
"""
作用: 将字符串进行切割
返回值 返回值是一个列表
参数: 按照什么方式来进行切割, 参数就是什么
result = my_str.split("/")
print(result)

"""
# capitalize
"""
作用: 把字符串的第一个字符大写
返回值: 字符串  没有参数
result = my_str.capitalize()
print(result)
"""
# title
"""
作用: 把每一个单词都进行大写
result = my_str.title()
print(result)

"""
# startswith
"""
作用: 检测字符串是以XXX开头
参数: "要检测的字符串"
返回值 : 布尔类型
result = my_str.startswith("hEllo")
print(result)
"""

# endswith
"""
作用: 监测字符串是以 XXX结尾
参数: 要检测的字符串
返回值: False True
result = my_str.endswith("p1")
print(result)
"""

# lower

"""
作用: 将字符串全部转化为小写
返回值: 字符串
result = my_str.lower()
print(result)

"""

# upper
"""
作用: 将字符串全部转化为大写
返回值: 字符串

result = my_str.upper()
print(result)

"""

# ljust
"""
作用: 原字符串左对齐,并使用空格填充至长度 width 的新字符串
参数: 返回新字符串的长度
返回值: 字符串
result = my_str.ljust(10)
print(len(result))
print(result)
"""

# rjust
"""
作用: 原字符串右对齐,并且使用空格来进去填充,
参数: 返回新字符串的长度
返回值: 字符串

result = my_str.rjust(40)
print(result)
"""

# center
"""
作用: 原字符串左右居中, 不够的时候使用空格,进行填充
参数: 新字符串的长度
返回值: 新的字符串

result = my_str.center(40)
print(result)
"""

# lstrip
"""
作用: 删除字符串左边空格字符
参数: 无
返回值: 新字符串
result = my_str.lstrip()
print(len(my_str))
print(len(result))
print(result)
"""

# rstrip
"""
作用: 删除字符串右边空格部分
参数: 无参数
返回值: 字符串
result = my_str.rstrip()
print("原来字符长度 %d " % len(my_str))
print("切割后字符串长度 %d" %len(result))
print(result)

"""

# strip
"""
作用: 删除左右两边的空格
参数: 无参数
返回值: 字符串
result = my_str.strip()
print("原来字符长度 %d " % len(my_str))
print("切割后字符串长度 %d" %len(result))
print(result)

"""
# rfind
"""
作用: 类似于find 不过是从右往左查找
参数: 要查找的内容
返回值: 要查找的下标
result = my_str.rfind("ello")
print(result)
"""
# rindex
"""
作用: 类似于index 不过是从右往左查找, 查到返回下标, 查不到报错
参数: 要查找的内容
返回值: 查找到的下标, 查找不到,报错
result = my_str.rindex("llo")
print(result)
"""
# partition
"""
作用: 将字符串进行三等分
参数: 以XXX来进行分割
返回值: 元组 xxx前, xxx, xxx后
result = my_str.partition('world')
print(result)
"""

# rpartition
"""
作用: 类似于partition 不过是从右开始向左分
参数: 以XXX进行分割
返回值: 元组 xxx前, xxx, xxx后
result = my_str.rpartition("world")
print(result)
"""
# splitlines
"""
作用: 按照换行来进行分割
参数: 无参数
返回值: 列表
result = my_str.splitlines()
print(result)
"""

# isalpha
"""
作用: 判断字符串是否全部由字母组成
返回值: True False
参数: 无参数
result = my_str.isalpha()
print(result)

"""

# isdigit
"""
作用: 判断字符串是否全部由数字组成
返回值: True False
参数: 无参数
result = my_str.isdigit()
print(result)
"""

# isalnum
"""
作用: 判断字符串是否全部由数字字母组成
参数: 无参数
返回值: True False

"""
# isspace
"""
作用: 判断字符串由空格组成
参数: 无
返回值: True False
result = my_str.isspace()
print(result)
"""
# join
"""
作用: 将列表中的内容转化为字符串
参数: 要转换的列表
返回值: 字符串
list = ["123", 'abc','adsadsa']
str = "D".join(list)
print(str)
"""
result = my_str.isalnum()
print(result)
