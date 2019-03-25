# 字典扁平化
dict2 = {'d': {'e': 3, 'f': {'g': 4}}, 'a': 5}
dict3 = {'d': {'e': 3, 'f': {'g': 4}}, 'a': 5, 'aa': 234, 'bb': {'cc': {'dd': { 'yy': 321, 'nn': 00}, 'nn': 88}}}

def counter(dict1):
    for k, v in dict1.items():
        if isinstance(v, dict):
            for text in counter(v):
                yield '{}.{}'.format(k, text)
        else:
            yield '{}={}'.format(k, v)

yy = counter(dict3)
for i in yy:
    print(i)



target = {}
def counter2(dict1, joint=''):
    for k, v in dict1.items():
        if isinstance(v, dict):
            counter2(v, joint+k+'.')
        else:
            target[joint+k] = v
counter2(dict3)
print(target)
