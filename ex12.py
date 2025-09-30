# How many times is a greater than b?

def times_bigger():

    a = int(input('Please, enter the first integer: '))
    b = int(input('Please, enter the second integer: '))
    if a == 0 or b == 0:
        return 'That does not make sense. We cannot divide by zero and times greater that zero does not make sense. You know it is going to be zero lol'
    if a > b:
        return a / b
    if b > a:
        return b / a
    if a == b:
        return 'b and a are equal numbers'


result = times_bigger()
print(result)
