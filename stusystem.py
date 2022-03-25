import os
import PyInstaller

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？（y/n）')
                if answer == 'y' or answer == 'Y':
                    print('谢谢使用！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                serch()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            pass  # 解决报错问题


def menu():
    print('===================学生信息管理系统====================')
    print('----------------------功能菜单------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-----------------------------------------------------')


def insert():  # 用于录入学生信息
    student_list = []
    while True:
        input1 = input('请输入学生的ID（如1001）')
        if not input1:
            break
        input2 = input('请输入学生的姓名')
        if not input2:
            break
        try:
            input3 = int(input('请输入英语成绩'))
            input4 = int(input('请输入Python成绩'))
            input5 = int(input('请输入Java成绩'))
        except:
            print('成绩无效，请重新输入！')
            continue

        student = {'id': input1, 'name': input2, 'english': input3, 'python': input4, 'java': input5}
        student_list.append(student)
        choice1 = input('是否继续添加：（y/n）')
        if choice1 == 'y' or choice1 == 'Y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入完成!')


def save(lst):  # 用于保存学生信息
    try:
        stu_txt = open(filename, 'a', encoding="utf-8")  # 加UTF-8防止中文乱码
    except:  # 出错改为直接写入？？
        stu_txt = open(filename, 'w', encoding="utf-8")  # filename作为已经申明的变量，不需要加引号
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def serch():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_txt = rfile.readlines()
    else:
        return
    flag1 = False
    while True:
        mode = int(input('按ID查找请输入1，按姓名查找请输入2：'))
        if mode == 1:
            stu_id = input('请输入学生ID：')
            if stu_id:
                for item in student_txt:
                    d = dict(eval(item))  # 将字符串转为字典
                    if d['id'] == stu_id:
                        flag1 = True  # 标记找到此学生了
                        show_one_stu(d)
                else:
                    if flag1:
                        flag1 = False
                        print('学生信息已打印！')
                    elif not flag1:
                        print('无此学生！')
            choice1 = input('是否继续查找：（y/n）')
            if choice1 == 'y' or choice1 == 'Y':
                continue
            else:
                break
        elif mode == 2:
            stu_name = input('请输入学生姓名：')
            if stu_name:
                for item in student_txt:
                    d = dict(eval(item))  # 将字符串转为字典
                    if d['name'] == stu_name:
                        flag1 = True  # 标记找到此学生了
                        show_one_stu(d)
                else:
                    if flag1:
                        flag1 = False  # 重置标志位，便于下次查找
                        print('学生信息已打印！')
                    elif not flag1:
                        print('无此学生！')
            choice2 = input('是否继续查找：（y/n）')
            if choice2 == 'y' or choice2 == 'Y':
                continue
            else:
                break
        else:
            print('查找模式错误，请重新输入')
            continue


def delete():
    while True:
        student_id = input('请输入要删除的学生的id：')
        if student_id:  # 确认输入了一个id
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记，表示还未删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True  # 标记，表示已经删除
                    if flag:
                        print(f'id为{student_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息！')
                break
        show()  # 删除中=后显示剩下的所有有学生信息
        answer = input('是否继续删除？（y/n）')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    while True:
        student_id = input('请输入需要修改学生的id：')
        if student_old:
            flag = False
            with open(filename, 'w', encoding='utf-8') as wfile:
                for item in student_old:
                    d = dict(eval(item))  # 将字符串转为字典
                    if d['id'] == student_id:
                        print('已经找到这名学生，可以修改相关信息！')
                        flag=True #表示有这名学生
                        while True:  # while与break配合才可以更好的构成循环
                            try:
                                d['name'] = input('请输入学生的姓名')
                                d['english'] = int(input('请输入英语成绩'))
                                d['python'] = int(input('请输入Python成绩'))
                                d['java'] = int(input('请输入Java成绩'))
                            except:
                                print('输入有误，请重新输入！')
                            else:
                                break
                        wfile.write(str(d) + '\n')

                    else:
                        wfile.write(str(d) + '\n')

            if flag==True:
                print('修改成功！')
            else:
                print("查无此人！")

        answer = input('是否继续修改？（y/n）')
        if answer == 'y' or answer == 'Y':
            modify()
        else:
            break
        break


def sort():
    global asc_or_desc_bool
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_lst = file.readlines()
        stu_new = []
        for item in student_lst:
            d = dict(eval(item))
            stu_new.append(d)
    else:
        return

    asc_or_desc = input('请选择(0.升序 1.降序）：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入有误，请重新输入！')
        sort()
    mode = input('0.按学号排序 \n1.按英语成绩排序 \n2.按Python成绩排序 \n3.按Java成绩排序 \n4.按总成绩排序\n请选择排序方式：')
    if mode == '0':
        stu_new.sort(key=lambda stu_new: int(stu_new['id']),
                     reverse=asc_or_desc_bool)  # key是列表中的关键字，配合lambda来选定用于排序的关键字
    elif mode == '1':
        stu_new.sort(key=lambda stu_new: int(stu_new['english']), reverse=asc_or_desc_bool)  # reverse用于确定升序或者降序，其值为布尔值
    elif mode == '2':
        stu_new.sort(key=lambda stu_new: int(stu_new['python']),
                     reverse=asc_or_desc_bool)  # 括号中的stu_new表示字典stu_new，因为前面已经申明是哪个字典了，所以在括号内可以用任意字母（如x）替换
    elif mode == '3':
        stu_new.sort(key=lambda stu_new: int(stu_new['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        stu_new.sort(key=lambda x: (int(x['english']) + int(x['python']) + int(x['java'])), reverse=asc_or_desc_bool)
    else:
        print('输入错误，请重新输入！')
        sort()

    stu_txt = open(filename, 'w', encoding="utf-8")  # filename作为已经申明的变量，不需要加引号
    for item in stu_new:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()
    show()


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as r_file:
            student_txt = r_file.readlines()
    else:
        return
    total = 0
    for item in student_txt:
        d = dict(eval(item))  # 将字符串转为字典
        if d['id']:
            total += 1
    print(f'一共有{total}名学生')


def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as r_file:
            student_txt = r_file.readlines()
    else:
        return
    format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    format_data = '{:^6}\t{:^7}\t{:^5}\t{:^10}\t{:^10}\t{:^13}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    for item in student_txt:
        d = dict(eval(item))  # 将字符串转为字典
        if d['id']:
            print(format_data.format(d['id'], d['name'], d['english'], d['python'], d['java'],
                                     str(int(d['english']) + int(d['python']) + int(d['java']))))


def show_one_stu(d):  # 姓名为中文可以对齐，英文会错位
    format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    format_data = '{:^6}\t{:^7}\t{:^5}\t{:^10}\t{:^10}\t{:^13}\t'
    print(format_data.format(d['id'], d['name'], d['english'], d['python'], d['java'],
                             str(int(d['english']) + int(d['python']) + int(d['java']))))


if __name__ == '__main__':
    main()
