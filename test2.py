#第一题
n = float(input("请输入距离："))
if n <= 3:
    m = 8
else:
    m = 1.3 * n + 1
print("价格：",round(m))

#第二题
import math
a = float(input("请输入二次项系数："))
b = float(input("请输入一次项系数："))
c = float(input("请输入常数项："))
m = b**2 - 4*a*c
if m == 0:
    print("方程有唯一一个实根：",-b / 2*a)
elif m < 0:
    print("方程无实根")
else:
    n = math.sqrt(m)
    print("方程有两个实根：",-b + n / 2*a, -b + n / 2*a)