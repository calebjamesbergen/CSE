# Do not forgot to compare responses to "1" not just 1
inventory = ["Stick,", "Leather armor"]
bare_hand_damage = 1
stick_damage = 2
leather_armor_defense = 1
eldrazi_scion_health = 1
eldrazi_scion_attack = 0
eldrazi_scout_health = 5
eldrazi_scout_attack = 1
total_health = 5
damage_taken = 0
total_gold = 0

alive_round1 = True
map_item = "Raven Gorge"
a = input("Hello human")
b = input("It is I")
c = input("You have a mission")
d = input("Take back the world from the evil eldrazi")
e = input("What would you like to do")
while alive_round1:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print(*inventory, sep=" ")
    elif beginning_choice == "2":
        print(map_item)
        print("Would you like to go to Raven Gorge")
        decision2 = input("1: Yes 2: No")
        if decision2 == "1":
            print("You are now in Raven Gorge")
            print("An eldrazi scion has appeared")
            print("What would you like to do?")
            decision3 = input("1: Attack 2: Run")
            if decision3 == "1":
                print("What would you like to attack with?")
                decision4 = input("1: Bare hands 2: Stick")
                if decision4 == "1":
                    eldrazi_scion_health -= 1
                elif decision4 == "2":
                    eldrazi_scion_health -= 2
            if eldrazi_scion_health <= 0:
                print("You won")
                total_gold += 5
                print("You now have %s gold" % total_gold)
            if decision3 == "2":
                alive_round1 = False
            print("Oh no! An eldrazi scout has appeared")
            decision5 = input("1: Fight 2: Run")
            if decision5 == "2":
                alive_round1 = False
            while eldrazi_scout_health > 0 and not decision5 == "2":
                if decision5 == "1":
                    print("What would you like to attack with?")
                    decision6 = input("1: Bare hands 2: Stick")
                    if decision6 == "1":
                        eldrazi_scout_health -= 1
                    elif decision6 == "2":
                        eldrazi_scout_health -= 2
                total_health -= eldrazi_scout_attack
                print("The eldrazi scout now has %s health" % eldrazi_scout_health)
                print("You have %s health left" % total_health)
            print("You won")
            total_gold += 10
            print("You now have %s gold" % total_gold)
