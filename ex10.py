# In a 3×3 square, the sums of the numbers in each column, each row, and each diagonal
# (containing three cells) must all be equal. Find the number that should replace the asterisk. top middle cell
square = [
    [10, None, None],
    [9, None, 13],
    [14, None, None]
]
magic_sum = square[0][0] + square[1][0] + square[2][0]

square[1][1] = magic_sum - square[1][0] - square[0][2]
square[0][2] = magic_sum - square[2][0] - square[1][1]
square[0][1] = magic_sum - square[0][0] - square[0][2]
print(f'The solution for top middle cell is {square[0][1]}')
