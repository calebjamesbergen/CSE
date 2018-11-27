inventory = ["Stick", "Leather Armor"]
stick_damage = 1
leather_armor_defense = 1
alive = True
map_item = "Raven Gorge"
a = input("Hello human")
b = input("It is I")
c = input("You have a mission")
d = input("Take back the world from the evil eldrazi")
e = input("What would you like to do")
while alive:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print(inventory)
    elif beginning_choice == "2":
        print(map_item)
        print("Would you like to go to Raven Gorge")
        decision2 = input("3: Yes 4: No")
        if decision2 == 3:
            print("You are now in Raven Gorge")
            print("An eldrazi scion has appeared")
            print("What would you like to do?")
            decision3 = input("5: Attack 6: Run")
            if decision3 == 5:
                print()
            elif decision3 == 6:
                print("You die")
                alive = False
print("You died")
