db_file = 'student_data.db'

def register_api():
    stu_data = {}  # 存储用户数据的字典
    print('欢迎使用注册'.center(50, '-'))
    print('请完成信息完善')
    
    # 输入信息（修复 strip() 并添加年龄校验）
    name = input('姓名:').strip()
    
    age = input('年龄:')
    if not age.isdigit():
        exit("年龄必须为数字！")
    age = int(age)
    
    phone = input('手机号:').strip()  # ✅ 修复括号
    id_num = input('身份证号:').strip()  # ✅ 修复括号
    
    # 课程选择
    course_list = ['python', 'linux', '网络安全', '数据分析', '网络安全']
    for index, course in enumerate(course_list):
        print(f'{index}. {course}')
    
    selected_course = input('选择想学的课:')
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if 0 <= selected_course < len(course_list):
            picked_course = course_list[selected_course]
        else:
            exit('编号不合法')
    else:
        exit('非法输入')
    
    # 存入字典（添加 phone 字段）
    stu_data['name'] = name
    stu_data['age'] = age
    stu_data['phone'] = phone  # ✅
    stu_data['id_num'] = id_num
    stu_data['course'] = picked_course
    
    return stu_data

def commit_to_db(filename, stu_data):
    with open(filename, 'a', encoding='utf-8') as f:  # ✅ 指定编码
        row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}\n"  # ✅
        f.write(row)

student_data = register_api()
print(student_data)
commit_to_db(db_file, student_data)