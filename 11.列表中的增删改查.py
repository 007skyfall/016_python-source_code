# 列表中存放的数据是可以进行修改的，比如"增"、"删"、"改"、"查"

"""
增加元素
("增"append, extend, insert)

append : 尾部添加元素
name_list.append("xiaolv")

print(name_list)
extend : 将一个列表中的元素逐一添加到列表中区

name_list.extend(class_list)
print(name_list)
name_list.insert(1,"小白")
print(name_list)

修改
修改方式: name[0] = ""

查找元素("查"in, not in, index, count)

in（存在）,如果存在那么结果为true，否则为false
not in (不存在), 如果不存在那么结果为true，否则false
index : 返回下标
count

列表元素的常用删除方法有：

del：根据下标进行删除
del name_list[1]
print(name_list)
pop：删除最后一个元素
name_list.pop()
print(name_list)

remove：根据元素的值进行删除
name_list.remove("a")
print(name_list)

"""

name_list = ["c","b","a","c","b","a","c","b","a"]
class_list =["一年级","二年级"]

# name_list[0] = "小明"
#
# print(name_list)
# print("小明1" not in name_list)
# if "小明1" not in name_list:
#     print("今晚吃鸡腿")
#
# # index
# print(name_list.index("a"))
# # count
# num = name_list.count("a")
# print(num)

name_list.remove("a")
print(name_list)

# 列表嵌套
"""
定义: 列表中含有列表
取出北京大学
"""

schoolNames = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]

print(schoolNames[0][0])


