name = 'observer'

import pandas as pd
import string as str
import re

def read_students(x):
    
    table = pd.read_html(x, encoding = 'UTF-8')
    students = pd.DataFrame(table[1])
    students.fillna('100%', inplace = True)
    
    for i in range(2, students.shape[1]):
        students[i] = students[i].str.strip('%').astype(float)/100

    Lessons = list(table[0].loc[1])  
    re_lesson_1 = re.compile('Lesson 1$')
    idx = []
    for i in range(len(Lessons)):
        temp = re_lesson_1.findall(Lessons[i])
        if len(temp) == 1:
            idx.append(i)
    idx.append(len(Lessons))

    rep = []
    for i in range(1, len(idx)):
        rep.append(idx[i] - idx[i - 1])

    re_parts = re.compile('^Part \d+')
    Parts = []
    for i in range(len(table[0].loc[0].dropna())):
        temp = re_parts.findall(table[0].loc[0].dropna()[i])
        if len(temp) == 1:
            Parts.append(temp[0])

    headers = []
    for i in range(len(rep)):
        headers.extend([Parts[i]] * rep[i])

    Headers = []
    for i in range(len(headers)):
        Headers.append(headers[i] + ' ' + Lessons[i]) 

    Columns = list(table[2]) + Headers
    students.columns = Columns

    return students


def assign_status(x, student, projects, status):
    students_idx = x[x['Name'].isin([student])].index
    projects_idx = x[projects].columns
    x.loc[students_idx, projects_idx] = status
    return x

class Schedule:
    def __init__():
        