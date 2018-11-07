import random
money_total = 15
highest_money_gotten = 15
rounds_played = 0
total_money_over_time = 15
while money_total > 0:
    # play = input("Do you want to bet 1 dollar?")
    money_total -= 1
    rounds_played += 1
    die1 = (random.randint(1, 6))
    die2 = (random.randint(1, 6))
    dice_total = die1 + die2
    if money_total > highest_money_gotten:
        highest_money_gotten = money_total
    print("You rolled %s" % dice_total)
    if die1 + die2 == 7:
        money_total += 5
        total_money_over_time += 5
        print("You got a seven!!!")
    print("You have $%s" % money_total)
    print("You have played %s rounds" % rounds_played)
print("You got %s dollars" % total_money_over_time)
print("The most money you had was $%s" % highest_money_gotten)
