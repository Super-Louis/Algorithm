from timeit import Timer
import random

def insert_sort(list):
    """
    直接插入排序
    认为序列第一个值为已排好的序列
    对于每个未排序数据，在已排序序列中从后向前扫描，
    找到相应位置并插入。
    时间复杂度：O(n2)
    空间复杂度：O(1)
    :param list: list
    :return: sorted-list
    """
    for i in range(1, len(list)): # 第i次插入，共需进行len(list)-1次插入
        for j in range(0, i): # 每次插入需将list[i]与前面i-1个值依次进行比较(从右往左)
            if list[i-j] < list[i-j-1]: # 如果小于则交换位置
                list[i-j], list[i-j-1] = list[i-j-1], list[i-j]
            else: # 如果大于则跳出该次插入（前面已有序）
                break
    return list

def binary_search(list, value, end):
    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if list[middle] >= value:
            right = middle - 1
        else:
            left = middle + 1

    return left if left < end else -1

def binary_search_test(list, value):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if list[middle] > value:
            right = middle - 1
        elif list[middle] < value:
            left = middle + 1
        else:
            return middle

    return None

def insert_sort2(list):
    """
    直接插入排序
    在有序序列中查找元素可使用二分法，
    减少比较次数
    实测时间效率比直接插入低 => O(n(log2n+n))
    :param list: list
    :return: sorted-list
    """
    for i in range(1, len(list)): # 第i次插入，共需进行len(list)-1次插入
        tmp = list[i]
        index = binary_search(list, tmp, i)
        if index != -1:
            for j in range(i-index): # 从右往左重新赋值(如果从左往右,list[1] = list[0], list[2] = list[1],相当于重复赋值
                list[i-j] = list[i-j-1] # list[i] = list[i-1] => list[index+1] = list[index]
            list[index] = tmp
    return list

if __name__ == '__main__':
    list = [random.randint(1,10000) for _ in range(10000)]
    print(insert_sort2(list))
    # print(binary_search_test(list, 9))
    t2 = Timer("insert_sort2({})".format(list), "from __main__ import insert_sort2")
    print("insert_sort2 ", t2.timeit(number=1000), "milliseconds")

    # print(binary_search([1,3,5,6,8], 8))
