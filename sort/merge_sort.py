def merge_sort(list):
    """
    并归排序
    时间复杂度O(nlogn)
    空间复杂度O(n)
    :param list:
    :return:
    """
    if len(list) <= 1:
        return list
    n = len(list) // 2
    left = merge_sort(list[:n]) # 递归地将左边二分，直至只剩一个元素
    right = merge_sort(list[n:]) # 递归地将右边二分，直至只剩一个元素
    return merge(left, right) # 将左右两边合并

def merge(left, right):
    """相当于两个有序列表进行合并"""
    l, r = 0, 0 # 左右序列的初始指针
    result = []
    while l < len(left) and r < len(right): # 如果指针小于长度则进行while循环
        if left[l] < right[r]: # 如果左边小于右边，则将左边指针对应的元素加入list，并将左边指针右移
            result.append(left[l])
            l += 1
        else:
            result.append(right[r]) # 如果右边小于左边，则将右边指针对应的元素加入list，并将、右边指针右移
            r += 1
    result.extend(left[l:]) # 当任何一边的遍历完之后，将剩余元素加入list
    result.extend(right[r:])
    return result

if __name__ == '__main__':
    print(merge_sort([0,1,0,1,2,1,3,5]))
    """
    [0,1,0,1] [2,1,3,5]
    [0,1] -- [0,1]; [2,1] -- [3,5]
    [0] [1] merge -- [0] [1] merge; [2] [1] merge -- [3] [5] merge
    [0,1] merge [0,1]; [1,2] merge [3,5]
    [0,0,1,1] merge [1,2,3,5]
    [0,0,1,1,1,2,3,5]  
    """