# You are given a number n. The number n can be negative or positive.
def printing_the_array():
    n = int(input('Please, enter the desireable number: '))
    if n < 0:
        print(list(range(n, 1)))
    if n > 0:
        print(list(range(n-1, -1, -1)))
    if n == 0:
        print('This array cannot be printed.')


printing_the_array()
# If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
# If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
# Note:- You don't have to return anything, you just have to print the array.


def pos(n):
    # Positive n: print from n-1 down to 0 in one line
    for i in range(n-1, -1, -1):
        print(i, end=' ')
    print()  # optional: move to next line after printing


def neg(n):
    # Negative n: print from n up to 0 in one line
    for i in range(n, 1):  # n to 0 inclusive
        print(i, end=' ')
    print()
# And thats the one that I did later and it was accepted


def pos(n):
    # Write the code
    if n > 0:
        arr = list(range(0, n))
        print(*arr[::-1])


def neg(n):
    # Write the code
    if n < 0:
        arr = list(range(n, 1))
        print(*arr)
# Their solutiondef pos(n):
    n -= 1
    while n >= 0:
        print(n, end=' ')
        n -= 1


def neg(n):

    while n <= 0:
        print(n, end=' ')
        n += 1
