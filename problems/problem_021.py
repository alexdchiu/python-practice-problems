# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"
#
# There is pseudocode to guide you.

def gear_for_day(is_workday, is_sunny):
    # Create an empty list that will hold the different gear
    # gear = new empty list
    gear = []
    # If it is a workday and it is not sunny
        # Add "umbrella" to gear
        # gear.append("umbrella")
    if is_workday == True and is_sunny == False:
        gear.append("umbrella")
    # If it is a workday
        # Add "laptop" to gear
    if is_workday == True:
        gear.append("laptop")
    # Otherwise
        # Add "surfboard" to gear
    if is_workday == False:
        gear.append("surfboard")
    # Return the list of gear
    return gear
