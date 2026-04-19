#第一题
N = int(input("请输入一个大于等于0小于等于1000的整数："))
for x in range(N//3+1):
    for y in range((N - 3*x)//2+1):
        z  = (N - 3*x - 2*y)*2
        if (x + y + z)==N:
            print("大马：",x,"中马：",y,"小马：",z)
print("END")    
#第二题
M = int(input("请输入一个大于等于0小于等于1000的整数："))
i = 2
print("质因数为")
while M >= 4:
    while M % i == 0:
        print(i,end="")
        M //= i
        i += 1
if M > 1:
    print(M,end="")
