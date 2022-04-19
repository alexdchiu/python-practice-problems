# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.
#
# There is some pseudocode to guide you.

def remove_duplicate_letters(s):
    # result = new empty string
    result = ''
    # for every letter in the string s
        # if the letter is not in the result
            # add it to the end of the result
    for letter in s:
        if letter not in result:
            result = result + letter
    # return the result
    return result
    pass
