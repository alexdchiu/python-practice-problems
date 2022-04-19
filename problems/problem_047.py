# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    lower_check = False
    for char in password:
        if char.islower() == True:
            lower_check = True
            break
    
    upper_check = False
    for char in password:
        if char.isupper() == True:
            upper_check = True
            break
    
    digit_check = False
    for char in password:
        if char.isdigit() == True:
            digit_check = True
            break

    special_char = ["$", "!", "@"]
    special_check = False
    for char in password:
        if (char in special_char) == True:
            special_check = True
            break
    # print(special_check)

    if lower_check == True and upper_check == True and digit_check == True and special_check == True and len(password) >= 6 and len(password) <= 12:
        return True
    else:
        return False
    pass
