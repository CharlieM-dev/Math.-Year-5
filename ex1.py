# make an algorithm that will return n number of natural numbers (integers)
def natural_numbers():
    # needs to accept the number from the user and create a sequense of integers
    x = int(input(
        'Please, enter the last number of the sequense you want to create: '))
    # needs to take the number and create the array from 0 to the number taken from user
    list_of_numbers = []
    n = 0
    while n <= x:
        list_of_numbers.append(n)
        n += 1
    return list_of_numbers


numbers = natural_numbers()
print(numbers)
