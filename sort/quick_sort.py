def qsort(list):
    return quick_sort(list, 0, len(list)-1)

def quick_sort(list, left, right):
    """
    快速排序
    先选定一个基准值(左指针对应的值)
    首尾设置两个指针，向中间逼近，
    如果左指针对应的元素大于基准值而右指针对应的元素小于基准值
    则交换左右指针的值
    当左右指针重合时，将重合点的值与基准值互换，完成对基准值的排序
    接下来对基准值左右的子集重复以上排序步骤，直至所有值完成排序
    时间复杂度：O(nlogn)
    :param list: 待排序列表
    :param left: 做左指针
    :param right: 右指针
    :return:
    """
    if left >= right: # 基线条件（跳出递归）
        return list
    l = left # 每次循环初始左指针
    r = right # 每次循环初始右指针
    base = list[l]
    while left < right:
        while list[right] >= base and left < right:
            right -= 1
        while list[left] <= base and left < right:
            left += 1
        list[left], list[right] = list[right], list[left] # 如果左指针对应的元素大于基准值而右指针对应的元素小于基准值，则交换左右指针的值
    list[left], list[l] = list[l], list[left] # 当左右指针重合时，将重合点的值与基准值互换，完成对基准值的排序
    quick_sort(list, l, left-1)
    quick_sort(list, right+1, r)
    return list

def quick_sort2(list):
    if len(list) <= 1: # 基线条件，跳出递归
        return list
    base = list[0]
    lar_b = [i for i in list[1:] if i >= base]
    low_b = [i for i in list[1:] if i < base]
    return quick_sort2(low_b) + [base] + quick_sort2(lar_b)

def quick_sort3(list):
    """todo: 使用堆栈实现快排"""
    pass

if __name__ == '__main__':
    print(qsort([1,3,2,0,1,1,3,4]))
    print(quick_sort2([1,3,2,0,1,1,3,4]))



