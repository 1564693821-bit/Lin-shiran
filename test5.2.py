print("请输入学生信息：")
students = []
while True:
    data = input().strip()
    if not data:
        break
    parts = data.split()
    if len(parts) == 3:
        id = int(parts[0])
        name = parts[1]
        score = int(parts[2])
        students.append([id,name,score])
    else:
        print("格式错误，请重新输入")
students.sort(key= lambda x:(-x[2],x[0]))
print("排序后的列表：")
for stu in students:
    print(stu)
students[0][2] += 5
print("第一名加分后信息",students[0])
new_student = [202500,"Chen",95]
students.insert(0,new_student)
print("插入新同学后的列表：")
for stu in students:
    print(stu)
students = [stu for stu in students if stu[2] >= 80]
print("删除成绩低于八十分后的列表")
for stu in students:
    print(stu)
#思考题回答
#上述操作中，元组无法实现排序，修改元素，插入元素，删除元素
#元组是不可变序列一旦创建不能修改
