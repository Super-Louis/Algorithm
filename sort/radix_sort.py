def radix_sort(input_list):
    """
    基数排序，先按个位进行排序，再按十位排序...
    时间复杂度O(digit*N)
    :param input_list:
    :return:
    """
    has_digit = True
    count = 0
    while has_digit: # 直到没有位数则跳出循环
        has_digit = False
        sorted_list = [list() for _ in range(10)] # 空的列表，用于存储0~9对应的数字
        for i in range(len(input_list)):
            digit = (input_list[i] // (10**count)) % 10 # 得到某一位的数值
            if digit:
                has_digit = True
            sorted_list[digit].append(input_list[i])
        input_list = new_list(sorted_list) # 得到按照某一位排序后的新列表
        count += 1
    return input_list

def new_list(input_list):
    # print(input_list)
    new_list = list()
    for i in range(len(input_list)):
        new_list += input_list[i]
    # print(new_list)
    return new_list

if __name__ == '__main__':
    print(radix_sort([1,20,11,5,333,0,232,2333333,645,555,789,4444]))