# what integer would be the next after n given by user?
def next_number():
    n = int(
        input('Please, enter the integer you would like to find the next number for: '))
    number = n + 1
    return number


x = next_number()
print(f'The next natutal number after your number is {x}')
