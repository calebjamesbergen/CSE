import csv


def validate(num: str):
    if is_it_odd(num) and is_it_even(num):
        return True
    return False


def is_it_odd(num: str):
    first_number = int(num[0])
    if first_number % 2 != 0:
        return True
    return False


def is_it_even(num: str):
    first_number = int(num[1])
    if first_number % 2 == 0:
        return True
    return False


def reverse_it(string):
    return string[::-1]


print(reverse_it("dlroW olleH"))

# with open("Book1.csv", "r") as old_csv:
# #     reader = csv.reader(old_csv)
# #
# #     for row in reader:
# #         old_number = row[0]
# #         print(old_number)
# #         new_number = int(old_number)
# #         new_number += 1
# #         print(new_number)
# #
# #
# #     # Or
# #
# #     for row in reader:
# #         old_number = row[0]
# #         print(int(old_number) + 1)

# 'r' means read only

# with open("Book1.csv", "r") as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if old_number[14] and not old_number[15]:
#                 writer.writerow(row)
#
#     print("Done")


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if validate(old_number):
                writer.writerow(row)

    print("Done")
