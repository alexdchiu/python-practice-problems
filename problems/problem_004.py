# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def max_of_three(value1, value2, value3):
    max = value1
    if value2 >= max:
        max = value2
    if value3 >= max:
        max = value3
    return max
    pass
