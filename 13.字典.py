"""
字典:
    在{键:值}
    内容: 键值对  键:值

访问 :通过键来进行访问
 key:vual
print(info["name"])
print(info.get("avc"))
get 访问会比较友好, 如果key不存在 ,不会直接报错
如果没有key 则会直接报错
修改:
info["name"] = 班花

添加:
同时添加键值对
info["abc"] = "班花"

删除
del :删除一个内容
clear() :清除所有内容

字典的常用操作
len
keys : 打印出所有的键
values
info.keys()
info.values()
info.items()

"""
info = {'name':'班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}

print(info.get("avc"))

info["abc"] = "班花"

print(info)

print(len(info))

print(info.keys())
print(info.values())
print(info.items())