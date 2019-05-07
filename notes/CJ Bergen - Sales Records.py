import csv
# Fruits, Clothes, Meat, Beverages, Office Supplies, Cosmetics, Snacks, Personal Care, Household, Vegetables, Baby Food, Cereal


def do_it(type_o_item, profits):
    print(type_o_item)
    print(profits)
    fruit_profits = is_it_fruit(type_o_item, profits)
    print(fruit_profits)


def is_it_fruit(type_item, profit1):
    fruit_profit = 0
    if type_item == "Fruits":
        fruit_profit += int(profit1)
    return fruit_profit


with open("Sales Records.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        listostuff = []

        for row in reader:
            type_of_item = row[2]
            profit = row[13]
            if type_of_item not in listostuff:
                listostuff.append(type_of_item)
            do_it(type_of_item, profit)
        print(listostuff)