"""
1.for循环的语法格式：
for 临时变量 in 待处理数据集（序列）
    循环满足时执行的代码
"""
total=0
name="itheima is a brand of itcast"
for x in name:
    if x == "a":
        total+=1
print(total)
"""
注意：1.for循环是遍历型循环：数据有多少个，就循环多少次
     2.不能自定义判断条件，只能被动依次取出数据
"""