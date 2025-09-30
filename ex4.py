# Write the algorithm that will return the number that comes before the natural number n
def before_num():
    user_input = input('Please, enter the integer: ')
    if user_input.isdigit():
        n = int(user_input)
        if n >= 1:
            number = n - 1
            return number
        else:
            print('There is no natural number before 0, please, enter valid number')
            return None
    else:
        print('The number you have entered is not valid, please, try again')
        return None


result = before_num()
print(result)
