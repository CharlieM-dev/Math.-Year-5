# In a physical education class, all 26 students lined up in a row. Petro was 14th from the left, and Olena was 20th from the right.
# How many students were standing between Petro and Olena? let petro = a and olena = b

total_students = 26
a = 14
b_from_the_right = 20
b_position = total_students - b_from_the_right + 1
in_between = abs(a - b_position) - 1
print(in_between)
