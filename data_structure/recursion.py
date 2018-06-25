def resum(list):
    if not list: # 基线条件
        return 0
    else: # 递归条件
        return list.pop() + resum(list)

def recount(list):
    if not list:
        return 0
    else:
        list.pop()
        return 1 + recount(list)

def remax(list):
    """
    递归找极大值
    时间复杂度：O(n)
    """
    max = list.pop()
    if not list:
        return max
    else:
        next = list.pop()
        if next >= max:
            max = next
        list.append(max)
        return remax(list)

# def refind(list, i, middle = None):# 二分排序通过递归实现？
#     low = 0
#     up = len(list) - 1
#     if not middle:
#         middle = int(1/2*(low+up))
#     if not list:
#         return None
#     elif i == list[middle]:
#         return middle
#     elif i > list[middle]:
#         low = middle + 1
#         return refind(list[low:up + 1], i, middle)
#     else:
#         up = middle_index - 1
#         return refind(list[low:up + 1], i, middle)

def qsort(list):
    """
    分而治之（D&C)；
    快速排序；
    时间复杂度：O(nlogn)
    """
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        large = list.pop()
        lower_group = [i for i in list if i <= large]
        larger_group = [i for i in list if i >= large]
        return qsort(lower_group) + [large] + qsort(larger_group)

print(qsort([1,2,4,3,5,2]))

# print(resum([]))
# print(recount([]))