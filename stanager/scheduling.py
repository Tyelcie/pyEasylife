name = 'scheduling'
from itertools import compress
import datetime

def parse_time(time, str_format = '%Y-%m-%d %H:%M'):
    parsed = datetime.datetime.strptime(time, str_format)
    return parsed

class Classes:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

def check_conflict(previous, proposal, rest):
    '''previous: list of tuples enveloping start time and end time
       current: list of tuples enveloping start time and end time'''
    buffle = datetime.timedelta(minutes = rest)
    checked = [not (prvs[0]>= proposal[1] + buffle or prvs[1] <= proposal[0] - buffle) for prvs in previous]
    conflict = list(compress(range(len(checked)), checked))
    conf_class = [previous[i] for i in conflict]
    return checked, conf_class

def check_available(available, proposal):
    checked = [avlb[0] <= proposal[0] and avlb[1] >= proposal[1] for avlb in available]
    occupation = list(compress(range(len(checked)), checked))
    return checked, occupation

def date_range(start, end):
    datelen = (scheduling.parse_time(end, str_format = '%Y-%m-%d') - scheduling.parse_time(start, str_format = '%Y-%m-%d')).days
    daterange = []
    for i in range(datelen+1):
        new_day = scheduling.parse_time(start, '%Y-%m-%d') + datetime.timedelta(days = i)
        daterange.append(new_day.strftime('%Y-%m-%d'))
    return daterange

class Mentor:
    def __init__(self, name, available, rest = 10, schedule = {}):
        '''available: list of tuples enveloping start time and end time'''
        self.name = name
        self.__reg_available = available.copy()
        self.available = available
        self.rest = rest
        self.min_per_day = min_per_day
        self.schedule = schedule
    def get_reg_available(self):
        return self.__reg_available
    
    def init_appointment(self, your_class, student, start):
        self.classes = your_class
        available_parse = [tuple(map(parse_time, (a, b))) for (a, b) in self.available]
        proposal = (parse_time(start), parse_time(start) + datetime.timedelta(minutes = your_class.duration))
        availability, occupation = check_available(available_parse, proposal)
        if any(availability):
            previous = np.concatenate(list(self.schedule.values())) if bool(self.schedule) else list(self.schedule.values())
            previous = [tuple(map(parse_time, (a, b))) for (a, b) in previous]
            conflict, conf_class = check_conflict(previous, proposal, self.rest)
            if any(conflict):
                conf_class = tuple(map(lambda x: x.strftime('%Y-%m-%d %H:%M'), conf_class))
                print('老师在{}-{}这段时间内有课，而且请给老师{}分钟休息时间，另行安排!'.format(conf_class[0], conf_class[1], self.rest))
            else:
                end = parse_time(start) + datetime.timedelta(minutes = self.classes.duration)
                print('没问题，该时间段内老师可排课！')
                if student.name not in self.schedule.keys():
                    self.schedule[student.name] = [(start, end.strftime('%Y-%m-%d %H:%M'))]
                else:
                    self.schedule[student.name].extend([(start, end.strftime('%Y-%m-%d %H:%M'))])
                # 剩余时间
                available_parse = [tuple(map(parse_time, (a, b))) for (a, b) in self.available]
                for i in occupation:
                    insertee = [(available_parse[i][0], parse_time(start)),
                                (end, available_parse[i][1])]
                    insertee = list(filter(lambda x: x[1] > x[0], insertee))
                    insertee = [tuple(map(lambda x: x.strftime('%Y-%m-%d %H:%M'), (a, b))) for (a, b) in insertee]
                    del self.available[i]
                    self.available[i:i] = insertee
        else:
            print('老师有安排了，请考虑以下时间段：\n{}'.format(self.available))
    def change_appointment(self, student, which, prop_start):
        prop_end = parse_time(prop_start) + datetime.timedelta(minutes = self.classes.duration)
        available_parse = [tuple(map(parse_time, (a, b))) for (a, b) in self.available]
        availability, occupation =  check_available(available_parse, (parse_time(prop_start), prop_end))
        if any(availability):
            previous = np.concatenate(list(self.schedule.values())) if bool(self.schedule) else list(self.schedule.values())
            previous = [tuple(map(parse_time, (a, b))) for (a, b) in previous]
            conflict, conf_class = check_conflict(previous, (parse_time(prop_start), prop_end), self.rest)
            conf_class = tuple(map(parse_time, conf_class))
            if any(conflict):
                print('老师在{}-{}这段时间内有课，而且请给老师{}分钟休息时间，另行安排!'.format(conf_class[0], conf_class[1], self.rest))
            else:
                print('没问题，该时间段内老师可排课！')
                self.available.append(self.schedule[student.name][which])
                self.available = sorted([x for x in self.available])           
                while any([self.available[i][0] == self.available[i-1][1] for i in range(1, len(self.available))]):
                    del_idx = list(filter(lambda i: self.available[i][0] == self.available[i-1][1], range(1, len(self.available))))
                    idx = list(filter(lambda i: not self.available[i][0] == self.available[i-1][1], range(1, len(self.available))))
                    idx.append(0)
                    for i in del_idx:
                        self.available[i-1] = (self.available[i-1][0], self.available[i][1])
                    self.available = sorted([self.available[x] for x in idx])
    
                self.schedule[student.name][which] = (prop_start, prop_end.strftime('%Y-%m-%d %H:%M'))

        else:
            print('老师有安排了，请考虑以下时间段：\n{}'.format(self.available))

class Student:
    def __init__(self, name, available, schedule = {}):
        self.name = name
        self.__reg_available = available.copy()
        self.available = available
        self.schedule = schedule
    def find_lecturer(self, lecturers):
        pass            