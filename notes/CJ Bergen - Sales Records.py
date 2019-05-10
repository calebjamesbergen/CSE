import csv
# Fruits, Clothes, Meat, Beverages, Office Supplies, Cosmetics, Snacks, Personal Care, Household, Vegetables, Baby Food, Cereal
# Sub-Saharan Africa, Middle East and North Africa, Australia and Oceania, Europe, Asia, Central America and the Caribbean, North America
# Region, highest rate of return


fruit_profit = 0
clothes_profit = 0
meat_profit = 0
beverages_profit = 0
office_supplies_profit = 0
cosmetics_profit = 0
snacks_profit = 0
personal_care_profit = 0
household_profit = 0
vegetables_profit = 0
baby_food_profit = 0
cereal_profit = 0

fruit_average = []
clothes_average = []
meat_average = []
beverages_average = []
office_supplies_average = []
cosmetics_average = []
snacks_average = []
personal_care_average = []
household_average = []
vegetables_average = []
baby_food_average = []
cereal_average = []

sub_saharan_africa_profit = 0
middle_east_and_north_africa_profit = 0
australia_and_oceania_profit = 0
europe_profit = 0
asia_profit = 0
central_america_and_the_caribbean = 0
north_america = 0


def do_it(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11, type12):
    num_lists = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12]
    if max(num_lists) == num1:
        return type1
    if max(num_lists) == num2:
        return type2
    if max(num_lists) == num3:
        return type3
    if max(num_lists) == num4:
        return type4
    if max(num_lists) == num5:
        return type5
    if max(num_lists) == num6:
        return type6
    if max(num_lists) == num7:
        return type7
    if max(num_lists) == num8:
        return type8
    if max(num_lists) == num9:
        return type9
    if max(num_lists) == num10:
        return type10
    if max(num_lists) == num11:
        return type11
    if max(num_lists) == num12:
        return type12


def do_it3(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11, type12):
    num_lists = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12]
    if max(num_lists) == num1:
        return type1
    if max(num_lists) == num2:
        return type2
    if max(num_lists) == num3:
        return type3
    if max(num_lists) == num4:
        return type4
    if max(num_lists) == num5:
        return type5
    if max(num_lists) == num6:
        return type6
    if max(num_lists) == num7:
        return type7
    if max(num_lists) == num8:
        return type8
    if max(num_lists) == num9:
        return type9
    if max(num_lists) == num10:
        return type10
    if max(num_lists) == num11:
        return type11
    if max(num_lists) == num12:
        return type12


def do_it2(num1, num2, num3, num4, num5, num6, num7, type1, type2, type3, type4, type5, type6, type7):
    num_lists = [num1, num2, num3, num4, num5, num6, num7]
    if max(num_lists) == num1:
        return type1
    if max(num_lists) == num2:
        return type2
    if max(num_lists) == num3:
        return type3
    if max(num_lists) == num4:
        return type4
    if max(num_lists) == num5:
        return type5
    if max(num_lists) == num6:
        return type6
    if max(num_lists) == num7:
        return type7


with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)

    region_list = []

    for row in reader:
        region = row[0]
        type_of_item = row[2]
        cost = row[8]
        profit = row[13]
        if type_of_item == "Fruits":
            fruit_profit += float(profit)
            fruit_average.append(float(profit) / float(cost))
        if type_of_item == "Clothes":
            clothes_profit += float(profit)
            clothes_average.append(float(profit) / float(cost))
        if type_of_item == "Meat":
            meat_profit += float(profit)
            meat_average.append(float(profit) / float(cost))
        if type_of_item == "Beverages":
            beverages_profit += float(profit)
            beverages_average.append(float(profit) / float(cost))
        if type_of_item == "Office Supplies":
            office_supplies_profit += float(profit)
            office_supplies_average.append(float(profit) / float(cost))
        if type_of_item == "Cosmetics":
            cosmetics_profit += float(profit)
            cosmetics_average.append(float(profit) / float(cost))
        if type_of_item == "Snacks":
            snacks_profit += float(profit)
            snacks_average.append(float(profit) / float(cost))
        if type_of_item == "Personal Care":
            personal_care_profit += float(profit)
            personal_care_average.append(float(profit) / float(cost))
        if type_of_item == "Household":
            household_profit += float(profit)
            household_average.append(float(profit) / float(cost))
        if type_of_item == "Vegetables":
            vegetables_profit += float(profit)
            vegetables_average.append(float(profit) / float(cost))
        if type_of_item == "Baby Food":
            baby_food_profit += float(profit)
            baby_food_average.append(float(profit) / float(cost))
        if type_of_item == "Cereal":
            cereal_profit += float(profit)
            cereal_average.append(float(profit) / float(cost))

        if region == "Sub-Saharan Africa":
            sub_saharan_africa_profit += float(profit)
        if region == "Middle East and North Africa":
            middle_east_and_north_africa_profit += float(profit)
        if region == "Australia and Oceania":
            australia_and_oceania_profit += float(profit)
        if region == "Europe":
            europe_profit += float(profit)
        if region == "Asia":
            asia_profit += float(profit)
        if region == "Central America and the Caribbean":
            central_america_and_the_caribbean += float(profit)
        if region == "North America":
            north_america += float(profit)

    fruit_averages = sum(fruit_average) / len(fruit_average)
    clothes_averages = sum(clothes_average) / len(clothes_average)
    meat_averages = sum(meat_average) / len(meat_average)
    beverages_averages = sum(beverages_average) / len(beverages_average)
    cosmetics_averages = sum(cosmetics_average) / len(cosmetics_average)
    office_supplies_averages = sum(office_supplies_average) / len(office_supplies_average)
    snacks_averages = sum(snacks_average) / len(snacks_average)
    personal_care_averages = sum(personal_care_average) / len(personal_care_average)
    household_averages = sum(household_average) / len(household_average)
    vegetables_averages = sum(vegetables_average) / len(vegetables_average)
    baby_food_averages = sum(baby_food_average) / len(baby_food_average)
    cereal_averages = sum(cereal_average) / len(cereal_average)

    average_list = [fruit_averages, clothes_averages, meat_averages, beverages_averages, cosmetics_averages, office_supplies_averages, snacks_averages, personal_care_averages, household_averages, vegetables_averages, baby_food_averages, cereal_averages]

    profit_list = [fruit_profit, clothes_profit, meat_profit, beverages_profit, office_supplies_profit, cosmetics_profit, snacks_profit, personal_care_profit, household_profit, vegetables_profit, baby_food_profit, cereal_profit]
    print("The total profit for fruits was $%f" % fruit_profit)
    print("The total profit for clothes was $%f" % clothes_profit)
    print("The total profit for meat was $%f" % meat_profit)
    print("The total profit for beverages was $%f" % beverages_profit)
    print("The total profit for office supplies was $%f" % office_supplies_profit)
    print("The total profit for cosmetics was $%f" % cosmetics_profit)
    print("The total profit for snacks was $%f" % snacks_profit)
    print("The total profit for personal care was $%f" % personal_care_profit)
    print("The total profit for household was $%f" % household_profit)
    print("The total profit for vegetables was $%f" % vegetables_profit)
    print("The total profit for baby food was $%f" % baby_food_profit)
    print("The total profit for cereal was $%f" % cereal_profit)
    print()
    typess = do_it(fruit_profit, clothes_profit, meat_profit, beverages_profit, office_supplies_profit, cosmetics_profit, snacks_profit, personal_care_profit, household_profit, vegetables_profit, baby_food_profit, cereal_profit, "Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal Care", "Household", "Vegetables", "Baby Food", "Cereal")
    print("The highest total profit was $%f and it was made by %s" % (max(profit_list), typess))

    profit_list2 = [sub_saharan_africa_profit, middle_east_and_north_africa_profit, australia_and_oceania_profit, europe_profit, asia_profit, central_america_and_the_caribbean, north_america]
    print()
    print("The total profit by Sub Saharan Africa was $%f" % sub_saharan_africa_profit)
    print("The total profit by Middle East and North Africa was $%f" % middle_east_and_north_africa_profit)
    print("The total profit by Australia and Oceania was $%f" % australia_and_oceania_profit)
    print("The total profit by Europe was $%f" % europe_profit)
    print("The total profit by Asia was $%f" % asia_profit)
    print("The total profit by Central America and the Caribbean was $%f" % central_america_and_the_caribbean)
    print("The total profit by North America was $%f" % north_america)
    typesss = do_it2(sub_saharan_africa_profit, middle_east_and_north_africa_profit, australia_and_oceania_profit, europe_profit, asia_profit, central_america_and_the_caribbean, north_america, "Sub-Saharan Africa", "Middle East and North Africa", "Australia and Oceania", "Europe",  "Asia", "Central America and the Caribbean", "North America")
    print()
    print("The highest total profit from a region was $%f and it was  made by %s" % (max(profit_list2), typesss))

    aaaa = do_it3(fruit_averages, clothes_averages, meat_averages, beverages_averages, office_supplies_averages, cosmetics_averages, snacks_averages, personal_care_averages, household_averages, vegetables_averages, baby_food_averages, cereal_averages, "Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal Care", "Household", "Vegetables", "Baby Food", "Cereal")
    print("The safest thing to invest in is %s with a %f ratio of 1 unit to the profit for that" % (aaaa, max(average_list)))
