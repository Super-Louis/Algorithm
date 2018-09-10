# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: merge_list.py
# Python  : python3.6
# Time    : 18-8-21 23:37

def merge_list(l1, l2):
    '''
    合并两个有序列表
    :param l1:
    :param l2:
    :return:
    '''
    l_new = []
    while (l1 and l2):
        if l1[0] <= l2[0]:
            l_new.append(l1[0])
            l1.remove(l1[0])
        else:
            l_new.append(l2[0])
            l2.remove(l2[0])
    if l1:
        l_new.extend(l1)
    if l2:
        l_new.extend(l2)
    return l_new

if __name__ == '__main__':
    print(merge_list([1,2,5],[2,3,5]))