# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: search.py
# Python  : python3.6
# Time    : 18-8-21 22:06

def binary_search(l, v):
    '''
    二分查找
    :param l: input list
    :return: index / False
    '''
    left = 0
    right = len(l) - 1
    middle = int((left+right)/2)
    while left <= right:
        if l[middle] == v:
            return middle
        if l[middle] > v:
            right -= 1
        else:
            left += 1
        middle = int((left+right)/2)
    return False

def matrix_search(s, v):
    '''
    矩阵查找
    有一个二维数组（杨氏矩阵）
    数组的每行从左到右是递增的，每列从上到下是递增的.
    在这样的数组中查找一个数字是否存在。
    :param l: input matrix
    :return: index / False
    '''
    i, j = 0, len(s[0])-1
    while i <= len(s) - 1 and j >= 0:
        if s[i][j] == v:
            return True
        elif s[i][j] < v:# 如果s[i][j] < v, 则i行全部小于v
            i += 1
        else: # 如果s[i][j] > v, 则j列全部大于v
            j -= 1
    return False

if __name__ == '__main__':
    print(binary_search([1,3,5,6,8], 8))
    # print(matrix_search([[1,3,5],[2,4,6],[5,7,8]], 2))
