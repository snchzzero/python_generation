def is_valid(line: str):
    if 4 <= len(line) <= 6 and line.isdigit() and line.count(' ') ==0:
        return True
    return False

print(is_valid('49 83'))