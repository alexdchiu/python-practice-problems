# RECALL RECALL RECALL RECALL RECALL RECALL RECALL RECALL RECALL
#
# THAT'S RIGHT! THIS IS A REPEAT FROM EARLIER! CAN YOU SOLVE
# IT WITHOUT LOOKING BACK?
#
# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.
#
# It used the built-in function reversed and the join method
# for string objects.

def is_palindrome(word):
    reverse_letters = reversed(word)
    reverse_word = "".join(reverse_letters)
    if reverse_word == word:
        return True
    else:
        return False
    pass
