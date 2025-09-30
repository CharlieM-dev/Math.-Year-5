# “Which number is missing in the sequence so that it represents a natural number series: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, ...?”
numbers = list(map(int, input(
    'Please, enter the array you want to find the missing number in (the numbers should be separated by space): ').split()))


def missing_num():
    missing = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] > 1:
            missing.append(numbers[i] + 1)
    return missing


result = missing_num()
print(f'The missing number(s) in the array is {result}')
