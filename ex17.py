# Given broken line ABCDE, where AB = 8, BC = 14, CD = 23, DE = 10 find the length of the broken line
def broken_line_length():
    line_name = input(
        'Please, enter the name of your broken line: ').strip().upper()
    segments = {line_name[i:i+2]: None for i in range(len(line_name)-1)}
    for seg in segments:
        value = int(
            input(f'Please, enter the length of each of your segments in cm ({seg}): '))
        segments[seg] = value
        print(
            f'So that is the broken line segments we have got so far {segments}')
        continue
    total_length = sum(segments.values())
    return total_length


result = broken_line_length()
print(f'The total length of your broken line is: {result}')
