def shell_sort(list):
    """
    希尔排序
    先将list以步长n分组，对每列数据进行排序，
    再将数据已n/2为步长进行分组并按列排序
    时间复杂度：O(NlogN)
    :param list:
    :return:
    """
    n = len(list) // 2
    while n >= 1:
        for i in range(n, len(list)):
            for j in range(i,0,-n):
                print(j-n)
                if list[j] < list[j-n]:
                    list[j], list[j-n] = list[j-n], list[j]
                else:
                    break
        n = n // 2
    return list

if __name__ == '__main__':
    print(shell_sort([1,1,0,0,2,3,5,4,7,9,6]))

    # 2,2,3
    # 1,2,1,
    # 6
