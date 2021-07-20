# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 17:42
# @Author   : Charon.

def search_property(obj, count, res, arr):
    if count > 8:
        return False
    count += 1
    if isinstance(obj, list):
        length = min(len(obj), 5)
        for i in range(length):
            if obj[i] == res:
                arr.append(i)
                return True
            ok = search_property(obj[i], count, res, arr)
            if ok:
                arr.append(i)
                return True
    elif isinstance(obj, dict):
        for k in obj:
            if k == res:
                # arr.append(k)
                return True
            ok = search_property(obj[k], count, res, arr)
            if ok:
                arr.append(k)
                return True
    else:
        return False


if __name__ == '__main__':
    arr = []
    obj = {'a': 1, 'b': {'aa': 1, 'bb': [1, 2, {'c': 1}]}, 'cc': {'ccc': {'dd': {'v': [5, 6, {'x': [7]}]}}}}
    target = 7
    search_property(obj, 0, target, arr)
    result = ''
    for i in arr[::-1]:
        result += f'[{i}]' if isinstance(i, int) else f'[\'{i}\']'
    # result += f'[\'{target}\']'
    print(result)
    # result = []
    # for target in arr[::-1]:
    #     if target == 'aa':
    #         result.append(target)
    #         break
    #     result.append(target)
    # print(result)
