# OrderedDIct module - collections module
# OrderedDict 모듈 : 순서를 가진 딕셔너리 객체

def sort_by_key(t):
    return t[0]

from collections import OrderedDict

# d = {}
# d['x'] = 100
# d['l'] = 500
# d['y'] = 200
# d['z'] = 300

# for k, v in d.items():
#     print(k, v)

d = OrderedDict()
d['x'] = 100
d['y'] = 500
d['z'] = 200
d['l'] = 300


for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v)
