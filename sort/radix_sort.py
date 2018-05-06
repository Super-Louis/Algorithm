def radix_sort(input_list):
    has_digit = True
    count = 0
    while has_digit:
        has_digit = False
        sorted_list = [list() for _ in range(10)]
        for i in range(len(input_list)):
            digit = (input_list[i] // (10**count)) % 10
            if digit:
                has_digit = True
            sorted_list[digit].append(input_list[i])
        input_list = new_list(sorted_list)
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
    print(radix_sort([1,20,33,11,0,16,13,333,222]))