from functools import cmp_to_key

def get_biggest(numbers: list[int]) -> int:
    if not numbers:
        return -1

    # Преобразуем все числа в строки для удобства сравнения
    strs = list(map(str, numbers))

    # Компаратор: a+b > b+a -> a раньше
    def compare(a: str, b: str) -> int:
        if a + b > b + a:
            return -1   # a перед b
        elif a + b < b + a:
            return 1    # b перед a
        else:
            return 0

    sorted_strs = sorted(strs, key=cmp_to_key(compare))
    result = ''.join(sorted_strs)

    # Случай, когда все числа были нулями (но в вашем списке такого нет)
    return int(result) if result[0] != '0' else 0


print(get_biggest([1, 2, 3]))
print(get_biggest([71, 61, 228, 72, 9, 3, 11, 7]))
print(get_biggest([7, 71, 72]))
print(get_biggest([0, 0, 0, 0, 0, 0]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))