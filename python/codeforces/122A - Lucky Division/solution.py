def check_lucky_number(number):
    lucky_digits = ['4', '7']
    numberli = list(number)
    
    # Check if all digits are lucky
    for digit in numberli:
        if digit not in lucky_digits:
            # If there's a non-lucky digit, check for "almost lucky"
            return check_almost_lucky_number(int(number))
    
    # If all digits are lucky, it's a lucky number
    return "YES"


def check_almost_lucky_number(number):
    lucky_status = "NO"  # Default status
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    
    # Check if the number is divisible by any lucky number
    for lucky_number in lucky_numbers:
        if number % lucky_number == 0:
            lucky_status = "YES"
            break  # No need to continue checking once we find a lucky number
    
    return lucky_status


# Input reading
number = input()
print(check_lucky_number(number))
