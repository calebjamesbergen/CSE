# 1st Challenge
def challenge1(firstname, lastname):
    print(lastname, firstname)


challenge1("John", "Doe")


# 2nd Challenge
def odd_or_even(number_odd_or_even):
    if number_odd_or_even % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")


odd_or_even(1)
# 3rd Challenge


def triangle_area(length, height):
    triangle = (length*height)/2
    print(triangle)


triangle_area(2, 2)


# 4th Challenge
def pos_neg_zero(number_pos_neg_zero):
    if number_pos_neg_zero > 0:
        print("The number is positive")
    elif number_pos_neg_zero == 0:
        print("The number is zero")
    elif number_pos_neg_zero < 0:
        print("The number is negative")


pos_neg_zero(0)
