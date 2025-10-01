# A two-digit number ends with 4. If you add to this number the number formed
# by writing its digits in reverse order, you get 99. Find the number.
for num in range(10, 100):
    if num % 10 == 4:
        reversed_num = int(str(num)[::-1])

        if num + reversed_num == 99:
            print(
                f'The number is {num} and the reversed number is {reversed_num}')
