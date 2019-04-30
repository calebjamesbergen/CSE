import csv


def validate(num: int):
    do_it(num)


def do_it(num):
    last_num = num[15]
    new_num = num[0:15]
    reversed_num = new_num[::-1]
    num1 = reversed_num

    odd_numbers = [int(num1[0]), int(num1[2]), int(num1[4]), int(num1[6]), int(num1[8]), int(num1[10]), int(num1[12]), int(num1[14])]

    for i in range(len(odd_numbers)):
        odd_numbers[i] *= 2

        if odd_numbers[i] > 9:
            odd_numbers[i] -= 9

        num1[0] = str(odd_numbers[0])
        num1[2] = odd_numbers[1]
        num1[4] = odd_numbers[2]
        num1[6] = odd_numbers[3]
        num1[8] = odd_numbers[4]
        num1[10] = odd_numbers[5]
        num1[12] = odd_numbers[6]
        num1[14] = odd_numbers[7]

    final_num = num1[0] + num1[1] + num1[2] + num1[3] + num1[4] + num1[5] + num1[6] + num1[7] + num1[8] + num1[9] + num1[10] + num1[11] + num1[12] + num1[13] + num1[14]

    if final_num % 10 == 0:
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
