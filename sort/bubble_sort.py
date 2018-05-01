"""
时间复杂度：算法中基本操作重复执行的次数，可反映算法执行快慢.
通常表示为问题规模n的函数， 如果执行次数为常数，则时间复杂度为O(1)
空间复杂度：算法在运行过程中临时占用存储空间大小的量度？
"""
"""
冒泡排序：
时间复杂度O(n2)
空间复杂度O(1)
是一种稳定算法
"""
def bubble_sort(list):
    """
    冒泡排序
    列表长度为n
    第k次循环找出第k大的值, 排在最后(共n-1次)
    每次循环对列表前n-k个值进行两两比较
    """
    for i in range(len(list)-1): # n个值，需要经过n-1次排序
        for j in range(len(list)-i-1): # 已有i个值排好序，最后一个不需要两两比较
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def bubble_sort1(list):
    """
    冒泡排序
    列表长度为n
    第k次循环找出第k大的值, 排在最后(共n-1次)
    每次循环对列表前n-k个值进行两两比较
    改进1：如果第一次循环后排序未发生变化则终止排序
    """
    flag = 0
    for i in range(len(list)-1): # n个值，需要经过n-1次排序
        for j in range(len(list)-i-1): # 已有i个值排好序，最后一个不需要两两比较
            if list[j] > list[j+1]:
                flag = 1
                list[j], list[j+1] = list[j+1], list[j]
        if not flag:
            break
    return list

def bubble_sort2(list):
    """
    冒泡排序
    列表长度为n
    第k次循环找出第k大的值, 排在最后(共n-1次)
    每次循环对列表前n-k个值进行两两比较
    改进2：记录每次遍历后最后发生交换的位置j, 将其设置为下次循环的上界
    """
    flag = 0
    n = len(list) - 1
    k = n
    for i in range(n):  # n个值，需要经过n-1次排序
        for j in range(k): # 已有n-j个值排好序，最后一个不需要两两比较
            if list[j] > list[j+1]:
                flag = 1
                list[j], list[j+1] = list[j+1], list[j]
                k = j # 每次循环将k设置为最后发生交换的j
        if not flag:
            break
    return list

if __name__ == '__main__':
    print(bubble_sort2([0, 1, 1, 2, 3, 3, 4, 5, 5]))
    print(bubble_sort2([1, 0, 2, 1, 4, 6, 4, 3, 1]))

