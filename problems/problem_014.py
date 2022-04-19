# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three
# items.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def can_make_pasta(ingredients):
    list = ["flour", "eggs", "oil"]
    count = 0
    for item in list:
        if item in ingredients:
            count = count + 1
    if count == 3:
        return True
    else:
        return False
    pass
