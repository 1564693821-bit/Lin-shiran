total_data = []
single_data = {}
while True:
    dd = input().strip()
    if not dd:
        break
    data = dd.split(',')
    if len(data) == 6:
        single_data['id'] = int(data[0])
        single_data['name'] = data[1]
        single_data['class_num'] = int(data[2])
        single_data['Chinese'] = int(data[3])
        single_data['Math'] = int(data[4])
        single_data['English'] = int(data[5])
        total_data.append(single_data.copy())
        single_data.clear()
    else:
        print("格式错误")
for student in total_data:
    print(student)
    total = student['Chinese'] + student['Math'] + student['English']
    avg = total / 3
    student['总分'] = total
    student['平均分'] = round(avg,2)
total_data.sort(key = lambda x: (-x['总分'],x['id']))
class_1 = {'student':[]}
class_2 = {'student':[]}
class_3 = {'student':[]}
count1 = 0
count2 = 0
count3 = 0
class1_total = 0
class2_total = 0
class3_total = 0
for student in total_data:
    if student['class_num'] == 1:
        count1 += 1
        class1_total += student['总分']
        class_1['student'].append(student)
        class_1['班级人数'] = count1
        class_1['班级总分'] = class1_total
        class_1['班级平均分'] = class1_total/count1
    elif student['class_num'] == 2:
        count2 += 1
        class2_total += student['总分']
        class_2['student'].append(student)
        class_2['班级人数'] = count2
        class_2['班级总分'] = class2_total
        class_2['班级平均分'] = class2_total/count2
    else:
        count3 += 1
        class3_total += student['总分']
        class_3['student'].append(student)
        class_3['班级人数'] = count3
        class_3['班级总分'] = class3_total
        class_3['班级平均分'] = class3_total/count3
subject_max = {'Chinses':[],'Math':[],'English':[]}
Chinese_max = 0
Math_max = 0
English_max = 0
for student in total_data:
    if student['Chinese'] > Chinese_max:
        Chinese_max = student['Chinese']
        subject_max['Chinses'].extend([Chinese_max,student['name']])
    elif student['Chinese'] == Chinese_max:
        subject_max['Chinses'].append(student['name'])
    elif student['Math'] > Math_max:
        Math_max = student['Math']
        subject_max['Math'].extend([Math_max,student['name']])
    elif student['Math'] == Math_max:
        subject_max['Math'].append(student['name'])
    elif student['English'] > English_max:
        English_max = student['English']
        subject_max['English'].extend([English_max,student['name']])
    elif student['English'] == English_max:
        subject_max['English'].append(student['name'])
print("学生排名表")
for student in total_data:
    print(student)
print("班级统计信息")
print("一班",class_1)
print("二班",class_2)
print("三班",class_3)
print("单科最高分信息")
print(subject_max)
        
