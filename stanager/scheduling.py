name = 'scheduling'
from itertools import compress

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