from typing import List


def index_of_nearest(numbers: List[int], number: int):
    if not numbers:
        return -1

    result = None
    min_index = None
    for i in range(len(numbers)):
        if result is None or abs(numbers[i] - number) < result:
            result = abs(numbers[i] - number)
            min_index = i
    return min_index


print(index_of_nearest([9, 5, 3, 2, 11], 4))