# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def calculate_sum(values):
    if len(values) == 0:
        return None
    sum = 0
    for num in values:
        sum = sum + num
    return sum
    pass
