# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one
import random

def specific_random():
  div_by_5_and_7 = []
  x = 10
  while x <= 500:
    if x % 5 == 0 and x % 7 == 0:
      div_by_5_and_7.append(x)
    x = x + 1
  print (div_by_5_and_7)
  end = len(div_by_5_and_7)
  rand_index = random.randint(0,end)
  result = div_by_5_and_7[rand_index]
  return result