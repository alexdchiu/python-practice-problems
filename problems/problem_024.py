# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    # If there are no items in the list of values
        # return None
    if len(values) == 0:
        return None
    # sum = 0
    sum = 0
    # for each item in the list of values
        # add it to the sum
    for num in values:
        sum = sum + num
    # return the sum divided by the number of items
    # in the list
    return sum / len(values)
    pass
