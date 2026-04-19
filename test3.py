#第一题
n = int(input("请输入一个正整数: "))
flag = 1  
if n <= 1:
    flag = 0
else:
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break

if flag == 1:
    print(n,"是素数")
else:
    print(n,"不是素数")
#第二题
sum = 0
for i in range(1, 501):
    if i % 2 == 1:
        sum += i
print("前500个自然数中奇数和为:",sum)
#第三题
num = 1
count = 0
while num <= 300:
    if num % 13 == 0:
        count += 1
    num += 1
print("300以内被13整除的正整数个数为:",count)
#第四题
total = 0
print("请输入整数:")
while True :
    a = int(input())
    if a == 0:
        break
    total += a
print("所有非0输入数的总和为:",total)