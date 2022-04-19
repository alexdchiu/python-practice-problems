# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_sum(values):
    # If there are no items in the list of values
        # return None
    if len(values) == 0:
        return None
    # sum = 0
    sum = 0
    # for each item in the list of values
        # add it to the sum
    for item in values:
        sum = sum + item
    # return the sum
    return sum
    pass
