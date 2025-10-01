# A two-digit number ends with 4. If you add to this number the number formed
# by writing its digits in reverse order, you get 99. Find the number.
# let ending of the number and sum are given by user
def numbers():
    ending = int(
        input('Please, enter the number that your 2-digit number ends with: '))
    sum_of_nums = int(input('Please, enter the sum of numbers: '))
    for num in range(10, 100):
        if num % 10 == ending:
            reversed_number = int(str(num)[::-1])
            if num + reversed_number == sum_of_nums:
                return f'The starting number is {num} and the reversed number is {reversed_number}'

    return f'There are no numbers that match the condition :('


result = numbers()
print(result)
