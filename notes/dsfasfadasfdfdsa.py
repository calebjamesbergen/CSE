import csv


def validate(num: str):
    new_num = drop_last_digit(num)
    print(new_num)
    reversed_num = reverse_numbers(new_num)
    print(reversed_num)
    multiplied_nums = str(multiply_odds(reversed_num))
    print(multiplied_nums)


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


def combine_nums(num, num2):
    pass


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