def digit_count(numbers: list) -> list:
    return sorted(set(int(number) for number in numbers if numbers.count(number) > 1))


print(*digit_count(input().split(' ')))