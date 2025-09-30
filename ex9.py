# Getting ready to visit his grandmother, Karlsson ate x jars of jam for breakfast,
# and 16 more for lunch. How many jars did Karlsson eat in total? Write a program that will calculate the total number, given that user knows x
def total_num():
    user_input = input('Please, enter the starting number: ')
    x = int(user_input)
    if x >= 0:
        x_later = x + 16
        total = x + x_later
        return total
    else:
        print('Invalid input, please, try again!')
        return None


result = total_num()
print(f'Total number is {result}')
