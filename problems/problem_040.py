# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.
#
# There is pseudocode to guide you.

def add_csv_lines(csv_lines):
    # result_list = new empty list
    result = []
    # for each item in the csv_lines
    for item in csv_lines:
        # pieces = split the item on the comma
        pieces = item.split(",")
        # line_sum = 0
        line_sum = 0
        # for each piece in pieces
        for piece in pieces:
            # value = convert the piece into an int
            value = int(piece)
            # add the value to sum
            line_sum = line_sum + value
        # append sum to the result_list
        result.append(line_sum)
    # return result_list
    return result
    pass
