# 5th Challenge
def circle(radius_area):
    return 3.14159265 * (radius_area ** 2)


print(circle(1.1))


# 6th Challenge
def volume(radius_volume):
    return (4/3) * (3.14159265 * (radius_volume**3))


print(volume(2))


# 7th Challenge
def integer_stuff(integer):
    return integer + (integer + integer) + (integer + integer + integer)


print(integer_stuff(2))


# 8th Challenge
def number_stuff(number):
    if number >= 1850 and number <= 2150:
        return "The number is within 150 of 2,000"
    elif number >= 2850 and number <= 3150:
        return "The number is within 150 of 3,000"


print(number_stuff(1850))
print(number_stuff(2850))
