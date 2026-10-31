"""
range语法1 range(num)表示从0开始到num结束（不含num本身）
        2 range(num1,num2)表示从num1开始到num2结束（不含num2本身）
        3 range(num1,num2,step)表示从num1开始到num2结束（不含num2本身）,步长以step值为准
"""
a=0
num=int(input("请输入num:"))
for i in range(1,num):
    if i % 2 == 0:
        a+=1
print(a)