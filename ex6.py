# In a physical education class, all 26 students lined up in a row. Petro was 14th from the left, and Olena was 20th from the right.
# How many students were standing between Petro and Olena? let petro = a and olena = b

def in_between():
    user_input1 = input('Please, enter the total number of students: ')
    user_input2 = input(
        'Please, enter the positiong of student 1 from the left: ')
    user_input3 = input(
        'Please, enter the positiong of student 2 from the right: ')
    if user_input1.isdigit() and user_input2.isdigit() and user_input3.isdigit():
        total = int(user_input1)
        a = int(user_input2)
        b_from_right = int(user_input3)
        if total >= a and total >= b_from_right >= 1:
            b_position = total - b_from_right + 1
            students_between = abs(a - b_position) - 1
            return students_between
        else:
            print(
                'Invalid input. The total must be greater than a and b. Please, try again!')
            return None
    else:
        print('Invalid input. All the numbers of input must be natural numbers eg. > 0. Please, try again!')


result = in_between()
if result is not None:
    print(f"There're {result} students inbetween.")
