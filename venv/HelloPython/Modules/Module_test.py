def print_Line(char, times):

    print(char * times)

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


name = "Testing_01"