# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def minimum_value(value1, value2):
    min = value1
    if value2 < value1:
        min = value2
    return min
