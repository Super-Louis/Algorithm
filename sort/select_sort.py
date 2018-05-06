def select_sort(list):
    """
    简单选择排序
    先找出第一个最小的，与第一个元素交换位置；
    再从剩下的元素里找出最小的与第二个元素交换位置；
    重复上述过程
    时间复杂度：O(N2)
    :param list:
    :return:
    """
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

if __name__ == '__main__':
    print(select_sort([2,1,3,4,5,4,0,3,0,8,7,6]))


