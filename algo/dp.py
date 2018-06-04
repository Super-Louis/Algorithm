# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: dp.py
# Python  : python3.6
# Time    : 18-6-3 21:47
# Github  : https://github.com/Super-Louis

def most_common_string(a, b):
    """
    得到两个字符串的最长公共子串及其长度
    时间复杂度: O(n2)
    空间复杂度: 4
    :param a:
    :param b:
    :return:
    """
    max_len = 0
    most_common_str = ''
    len_tabel = [[0 for _ in range(len(b))] for _ in range(len(a))] # 用于记录长度的table
    str_tabel = [['' for _ in range(len(b))] for _ in range(len(a))] # 用于记录公共子串的table
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]: # 相等时长度等于左上角长度+1，子串等于左上角子串+1
                len_tabel[i][j] = len_tabel[i-1][j-1] + 1 if (i and j) else 1
                str_tabel[i][j] = str_tabel[i-1][j-1] + a[i] if (i and j) else a[i]
                if len_tabel[i][j] > max_len: # 如果当前长度大于最大长度，则更新最大长度及最长子串
                    max_len = len_tabel[i][j]
                    most_common_str = str_tabel[i][j]
            else: # 不等时长度置为0，子串置为''
                len_tabel[i][j] = 0
                str_tabel[i][j] = ''
    return max_len, most_common_str

def most_common_set(a, b):
    """
    得到两个字符串的最长公共子序列及其长度(不需要连续)
    时间复杂度: O(n2)
    空间复杂度: 4
    :param a:
    :param b:
    :return:
    """
    max_len = 0
    most_common_str = ''
    len_tabel = [[0 for _ in range(len(b))] for _ in range(len(a))] # 用于记录长度的table
    str_tabel = [['' for _ in range(len(b))] for _ in range(len(a))] # 用于记录公共子串的table
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]: # 相等时长度等于左上角长度+1，子串等于左上角子串+1
                len_tabel[i][j] = len_tabel[i-1][j-1] + 1 if (i and j) else 1
                str_tabel[i][j] = str_tabel[i-1][j-1] + a[i] if (i and j) else a[i]
                if len_tabel[i][j] > max_len: # 如果当前长度大于最大长度，则更新最大长度及最长子串
                    max_len = len_tabel[i][j]
                    most_common_str = str_tabel[i][j]
            else: # 不等时长度置左或上邻的最大值，子串置为左或上邻长度最长的字符串
                len_tabel[i][j] = max(len_tabel[i-1][j], len_tabel[i][j-1]) if (i and j) else 0
                str_tabel[i][j] = sorted([str_tabel[i-1][j], str_tabel[i][j-1]]
                                         , key=lambda i:len(i), reverse=True)[0] if (i and j) else ''
    return max_len, most_common_str

def max_sum_set(a):
    """
    得到列表中和最大的子列表
    时间复杂度: O(n2)
    空间复杂度: 4
    :param a:
    :param b:
    :return:
    """
    # todo: 怎么得到子列表？
    max_ending_here = 0
    max_sum = 0
    for i in range(len(a)):
        max_ending_here += a[i]
        if max_ending_here <= 0:
            max_ending_here = 0
        if max_ending_here > max_sum:
            max_sum = max_ending_here

    return max_sum


if __name__ == '__main__':
    print(most_common_string('abcdef', 'abgdef'))
    print(most_common_set('abcdef', 'abgdef'))
    print(max_sum_set([1, -2, 3, -1,-1, 2, -1, 3]))



