def print_Line(char, times):

    print(char * times)

print_Line("*#", 8)
print_Line("hi ", 5)

def print_lines(char, times, rows):
    """print multiple lines

    :param char: delimiter
    :param times: number of delimiters
    :param rows: number of rows
    """
    row = 0

    while row < rows:

        print_Line(char, times)
        row += 1

print_lines("*", 20, 5)





