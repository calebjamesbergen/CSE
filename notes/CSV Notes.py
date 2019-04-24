import csv
a = 0

with open("Book1.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    """
    for row in reader:
        old_number = row[0]
        print(old_number)
        new_number = int(old_number)
        new_number += 1
        print(new_number)
    """

    # Or

    for row in reader:
        old_number = row[0]
        # print(int(old_number) + 1)
        a += 1
