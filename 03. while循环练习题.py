"""
计算1~100的累积和（包含1和100）
sum = 0
i = 1

while i <= 100:
    sum = sum + i
    i += 1
print("1~100的累积和为 sum = %d" % sum )
"""

"""
1~100的累积的偶数和

"""
sum = 0
i = 1

while i <= 100:
    #判断是不是偶数
    if i % 2 == 0:
        sum = sum + i
    i += 1
print("1~100的累积的偶数和 sum = %d" % sum)