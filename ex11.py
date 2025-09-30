# By how much is a greater than b?
def difference_result():
    a = int(input('Please, enter the integer: '))
    b = int(input('Please, enter the integer: '))
    if a > b:
        return a - b
    if b > a:
        difference = b - a
        return f'Since you have entered b as greater number, we performed b - a and got {difference} result'
    if a == b:
        return 'a and b are equal'


result = difference_result()
print(result)
