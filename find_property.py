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
