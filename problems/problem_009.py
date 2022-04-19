# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.
#
# Now, try it without the helper variables and recreate it.
#
# It used the built-in function reversed and the join method
# for string objects.

def is_palindrome(word):
    reversed_word_list = reversed(word)
    reversed_word = "".join(reversed_word_list)
    if reversed_word == word:
        return True
    else:
        return False
    pass
