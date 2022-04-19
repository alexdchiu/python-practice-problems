# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.
#
# Try to remember how you did the last exercise and
# do similarly, here.

def is_divisible_by_5(number):
    if number % 5 == 0:
        return "buzz"
    else:
        return number
    pass
