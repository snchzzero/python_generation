def group_max(count: int):
    digits = [i for i in range(1, count + 1)]

    result_dict = {}
    for digit in digits:
        sum_digits = sum([int(d) for d in str(digit)])
        if sum_digits not in result_dict:
            result_dict[sum_digits] = {digit}
        else:
            result_dict[sum_digits].add(digit)

    return len(max(list(result_dict.values()), key= lambda x: len(x)))



print(group_max(int(input())))