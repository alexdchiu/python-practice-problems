# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

# latin alphabet upper 65-90
# latin alphabet lower 97-122
def shift_letters(str):
  result = ""
  for letter in str:
    if letter == "Z":
      new_letter = "A"
    elif letter == "z":
      new_letter = "a"
    else:
      new_letter = chr(ord(letter) + 1)
    result = result + new_letter
  return result

