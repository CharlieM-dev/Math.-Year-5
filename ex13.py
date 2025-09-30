# List 5 consecutive natural numbers starting from a


def numbers():
    n = int(input('Please, enter diseriable integer: '))
    list_of_num = [n + 1, n + 2, n + 3, n + 4, n + 5]
    return list_of_num


result = numbers()
print(f'The range is {result}')
