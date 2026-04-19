print("请输入学生信息：")
students = ()
while True:
    data = input().strip()
    if not data:
        break
    parts = data.split()
    if len(parts) == 3:
        id = int(parts[0])
        name = parts[1]
        score = int(parts[2])
        student = (id,name,score)
        students = students + (student,)
    else:
        print("格式错误，请重新输入")
print("输出所有学生信息：")
for stu in students:
    print("学号：",stu[0],"姓名：",stu[1],"成绩：",stu[2])
total_score = 0
count = 0
for stu in students:
    total_score = total_score + stu[2]
    count +=1
average_score = total_score / count
print("平均成绩：",average_score)
max_score = 0
max_student = ()
for stu in students:
    if stu[2] > max_score:
        max_score = stu[2]
        max_student= (stu,)
    elif stu[2] == max_score:
        max_student = max_student + (stu,)
print("最高分：",max_score)
for stu in max_student:
    print("最高分学生学号:",stu[0],"姓名:",stu[1])
score_tuple = ()
for stu in students:
    score_tuple = score_tuple + (stu[2],)
print("成绩元组：",score_tuple)