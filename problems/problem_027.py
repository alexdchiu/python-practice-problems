# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#
# There is some pseudocode to guide you.

def max_in_list(values):
    # if there are no items in the values list
        # return None
    # max value = first item in the values list
    # for each item in the values list
        # if item is greater than the max value
            # max value = item
    # return the max value
    if len(values) == 0:
        return None
    max = values[0]
    for item in values:
        if item > max:
            max = item
    return max
    pass
