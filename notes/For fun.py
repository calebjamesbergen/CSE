# Do not forgot to compare responses to "1" not just 1
inventory = ["Stick,", "Leather armor"]
damage = 1
armor = 1
eldrazi_scion_health = 1
eldrazi_scion_attack = 0
eldrazi_scout_health = 5
eldrazi_scout_attack = 2
total_health = 5
total_gold = 0
decision9 = "1"
alive_round1 = True
did_you_beat_round_one = False
map_item = "Raven Gorge"
a = input("Press enter to scroll through dialogue")
b = input("Hello human")
c = input("It is I")
d = input("You have a mission")
e = input("Take back the world from the evil eldrazi")
f = input("What would you like to do")
while alive_round1 and not did_you_beat_round_one:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print(*inventory, sep=" ")
    elif beginning_choice == "2":
        print(map_item)
        print("Would you like to go to Raven Gorge?")
        decision2 = input("1: Yes 2: No")
        if decision2 == "1":
            print("You are now in Raven Gorge")
            print("An eldrazi scion has appeared")
            print("What would you like to do?")
            decision3 = input("1: Attack 2: Run")
            while eldrazi_scion_health > 0:
                if decision3 == "1":
                    print("What would you like to attack with?")
                    decision4 = input("1: Stick")
                    if decision4 == "1":
                        eldrazi_scion_health -= 2
            if eldrazi_scion_health <= 0:
                print("You won")
                total_gold += 5
                print("You now have %s gold" % total_gold)
            decision5 = input("1: Fight 2: Run")
            while eldrazi_scout_health > 0 and not decision5 == "2" and total_health > 0:
                if decision5 == "1":
                    print("What would you like to attack with?")
                    decision6 = input("1: Stick")
                    if decision6 == "1":
                        eldrazi_scout_health -= 2
                total_health -= eldrazi_scout_attack - armor
                print("The eldrazi scout now has %s health" % eldrazi_scout_health)
                print("You have %s health left" % total_health)
            if eldrazi_scout_health <= 0:
                print("You won")
                total_gold += 10
                print("You now have %s gold" % total_gold)
            print("Would you like to look in the shop")
            decision7 = input("1: Yes 2: No")
            while decision7 == "1" and decision9 == "1":
                print("Healing Potion: 2 Gold")
                print("Wood Sword: 8 Gold")
                print("Wood Armor: 8 Gold")
                print("What would you like to buy?")
                decision8 = input("1: Healing Potion 2: Wood Sword 3: Wood Armor")
                if decision8 == "1" and total_gold >= 2:
                    total_health += 2
                    total_gold -= 2
                    print("Now you have %s health" % total_health)
                elif decision8 == "2" and total_gold >= 8:
                    damage = 4
                    total_gold -= 8
                    inventory.append("Wood sword")
                    print("Now you deal 4 damage")
                elif decision8 == "3" and total_gold >= 8:
                    armor = 3
                    total_gold -= 8
                    print("Now you have 3 armor points")
                    inventory.append("Wood armor")
                print("You have %s gold left" % total_gold)
                print("Would you like to remain in the shop")
                decision9 = input("1: Yes 2: No")
            did_you_beat_round_one = True
if did_you_beat_round_one:
    print("You have survived round 1. Congrats. It's about to get harder though")
else:
    print("You died")
alive_round1 = True
did_you_beat_round_two = False
while alive_round1 and not did_you_beat_round_two:
    print("As I said, eveything is about to get a lot harder")
    print("You destroyed a couple of scouts but that is nothing compared to what is coming")
