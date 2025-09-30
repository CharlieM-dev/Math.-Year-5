# How many natural numbers are there in a sequence between a and b?
def number_amount():
    user_input_1 = input(
        'Please, enter the integer that your sequence start with: ')
    user_input_2 = input(
        'Please, enter the integer that your sequence end with: ')
    if user_input_1.isdigit() and user_input_2.isdigit():
        a = int(user_input_1)
        b = int(user_input_2)
        if a > 0 and b > 0:
            if b > a:
                count = b - a - 1
                return count
            else:
                print('b should be greater than a. Please, try again!')
                return None
        else:
            print('Both numbers must be natural numbers eg. > 0. Please, try again!')
            return None
    else:
        print('Invalid input. Please, try again!')
        return None


result = number_amount()
print(f'There are {result} number(s) in a sequence between a and b :)')
