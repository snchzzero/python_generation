def same_parity(numbers: list) -> list:
    if not numbers:
        return []

    expected_null = True if numbers[0] % 2 ==0 else False
    new_numbers = []
    for num in numbers:
        if expected_null and num % 2 == 0:
            new_numbers.append(num)
        elif not expected_null and num % 2 != 0:
            new_numbers.append(num)
    return new_numbers



print(same_parity([]))