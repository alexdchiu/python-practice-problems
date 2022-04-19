# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

def group_cities_by_state(list):
  result = {}
  for city in list:
    # separate city and state 
    split_cities = city.split(", ")
    for split_city in split_cities:
      key = split_city[1]
      value = split_city[0]
      if key in result == True:
        result[key].append(value)
      else:
        result[key] = value
    return result
    # use state as key identifier 
    # see if state already exists in result 
    # if state exists already, append city to list value for corresponding state key
