a=10
b=input("请输入第一次猜想的数字：")
if int(b)==a:
    print("恭喜第一次就猜对了！")
elif int(input("猜错了，再猜一次："))==a:
    print("猜对了。")
elif int(input("猜错了，再猜最后一次：") )==a:
    print("恭喜，最后一次结果，你猜对了。")
else:
    print("Sorry,猜错了。")
"""
易错：1.if和elif是一整组，中间不能插入别的同级代码
     2.if/elif冒号前面只能写判断，不能写变量赋值
     3.if_else组合语句由上至下依次判断且互斥执行
"""
