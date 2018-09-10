def shell_sort(list):
    """
    希尔排序
    先将list以步长n分组，对每列数据进行排序，
    再将数据已n/2为步长进行分组并按列排序
    ...
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

def shell_sort_2(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i] # 对temp进行排序，将其置于合适位置
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap] # 将大于temp的元素右移
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary

if __name__ == '__main__':
    print(shell_sort_2([1,1,0,0,2,3,5,4,7,9,6]))

    # 1 1 0 0 2
    # 3 5 4 7 9
    # 6

