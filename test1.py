#第一题
print('Hello World')

#第二题
#第一种方法
a = 3
b = 10
a,b = b,a
print(a,b)
#第二种方法
A = 3
B = 10
C = A
A = B
B = C
print(A,B)

#第三题
x = input("请输入：")
y = x.upper()
c = x.count('o')
d = x.replace('a','o').replace('b','o').replace('c','o')
print(y)
print(c)
print(d)