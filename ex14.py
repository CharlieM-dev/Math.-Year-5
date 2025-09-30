# List 5 consecutive natural numbers starting from a but in reverse

def numbers_in_reverse():
    a = int(input('Please, enter the integer: '))
    numbers = [a - 1, a - 2, a - 3, a - 4, a - 5]
    if a > 5:
        return numbers
    else:
        print('Unfortunately, I cannot return negative numbers, because they are not integers. Please, try entering higher number')
        return None


result = numbers_in_reverese()
print(result)
