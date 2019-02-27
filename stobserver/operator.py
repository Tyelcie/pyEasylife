name = 'operator'
import pandas as pd
import itchat as ic

def send_task_group(task_seq, msg_template, students_df):
    for i in range(1, len(students_df)):
        student = students_df['姓名'][i]
        userID = ic.search_friends(name=student)[0]['UserName']
        personal_task = students_df[task_seq][i]
        msg = msg_template.format(student, personal_task)
        ic.send(msg, userID)

def send_task_personal(student_name, task_seq, msg_template, students_df):
    stu_pos = list(filter(lambda x: students_df['姓名'][x] == student_name, students_df.index.tolist()))[0]
    msg = msg_template.format(student_name, students_df[task_seq][stu_pos])
    userID = ic.search_friends(name=student_name)[0]['UserName']
    ic.send(msg, userID)