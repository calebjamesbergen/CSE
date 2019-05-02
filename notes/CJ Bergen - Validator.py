import csv


def validate(num: str):
    new_num = drop_last_digit(num)
    reversed_nums = reverse_numbers(new_num)
    multiplied_nums = multiply_odds(reversed_nums)
    even_nums_list = even_nums(reversed_nums)
    test = 0
    sum1 = combine_nums(even_nums_list, multiplied_nums, test)
    true_or_false = mod_by10(sum1)
    if true_or_false:
        return True
    return False


def drop_last_digit(num):
    return num[0:15]


def reverse_numbers(num):
    return num[::-1]


def multiply_odds(num):
    list_num = []
    for i in range(len(num)):
        int_version = int(num[i])
        if i % 2 == 0:
            int_version *= 2
            if int_version > 9:
                int_version -= 9
            list_num.append(int_version)
    return list_num


def even_nums(num):
    return [int(num[1]), int(num[3]), int(num[5]), int(num[7]), int(num[9]), int(num[11]), int(num[13])]


def combine_nums(num, num2, num3):
    if num3 == num3:
        pass
    num3 = sum(num) + sum(num2)
    return num3


def mod_by10(sum3):
    if sum3 % 10 == 0:
        return True
    return False


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)

    print("Done")