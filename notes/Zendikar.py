import random


class MyClass:
    do_you_have_stick = True
    do_you_have_bronze_sword = False
    do_you_have_gold_sword = False
    do_you_have_silver_sword = False
    do_you_have_diamond_sword = False
    do_you_have_enchanted_sword = False
    do_you_have_leather_armor = True
    do_you_have_mail_armor = False
    do_you_have_silver_armor = False
    do_you_have_enchanted_armor = False
    do_you_have_the_pickaxe = False
    do_you_have_the_boat = False
    do_you_have_the_bottled_water = False

    did_you_buy_gold_sword = False
    did_you_buy_bronze_sword = False
    did_you_buy_silver_sword = False
    did_you_buy_diamond_sword = False
    did_you_buy_enchanted_sword = False
    did_you_buy_leather_armor = False
    did_you_buy_mail_armor = False
    did_you_buy_silver_armor = False
    did_you_buy_enchanted_armor = False

    alive_round1 = True
    alive_round2 = True
    did_you_beat_round_one = False
    did_you_beat_round_two = False
    skip_round_one = False
    skip_round_two = False
    did_you_beat_the_entire_game = False
    did_you_lose_the_entire_game = False
    did_you_get_to_the_mountain = False
    did_you_get_to_the_desert = False
    did_you_get_to_the_lake = False
    alive_in_the_mountain = True
    alive_in_the_lake = True
    alive_in_the_desert = True
    alive_in_the_cave = True
    did_you_get_to_the_cave = True
    did_you_find_the_cave = False
    did_you_beat_the_mountain = False
    did_you_beat_the_lake = False
    did_you_beat_the_desert = False
    did_you_beat_the_cave = False

    stick_damage = 1
    bronze_sword_damage = 3
    gold_sword_damage = 5
    silver_sword_damage = 10
    diamond_sword_damage = 15
    enchanted_sword_damage = 20
    leather_armor_defence = 1
    mail_armor_defence = 5
    silver_armor_defence = 10
    enchanted_armor_defence = 20
    damage = stick_damage
    armor = leather_armor_defence
    total_health = 5
    total_gold = 0

    stuff = ["Map, "]
    weapons = ["Stick, "]
    armors = ["Leather armor, "]
    map_item = []

    eldrazi_scion_health = 1
    eldrazi_scion_attack = 0
    eldrazi_scout_health = 5
    eldrazi_scout_attack = 2


you = MyClass()

decision9 = "1"
dec12 = "1"
dec13 = "1"
dec15 = "1"

input("Press enter to scroll through dialogue")
input("Welcome to the world of Zendikar")
input("This game will probably be more difficult than you will think")
input("If you die that is not my fault and try again")
input("If you want to smash the computer don't")
print()
print()
print()
b = input("Hello human")
if b == "Give me the money":
    you.total_gold += 1000000000000000000000000000000000
    print("You found it")
    print("You now have %s gold" % you.total_gold)
c = input("It is I")
if c == "Give me the money":
    you.total_gold -= 1000000000000000000000000000000000
    print("Ha, you failed")
    print("Now you have %s gold" % you.total_gold)
input("The all knowing")
print()
print()
print()
d = input()
if d == "Armor":
    you.armors.append("Mail Armor, ")
    you.do_you_have_mail_armor = True
    you.armors.append("Silver Armor, ")
    you.do_you_have_silver_armor = True
    you.armors.append("Enchanted Armor")
    you.do_you_have_enchanted_armor = True
    you.armor = you.enchanted_armor_defence
    print("Now you have these armors: %s" % "".join(you.armors))
input("Powerful")
print()
print()
print()
e = input()
if e == "Weapons":
    you.weapons.append("Wood Sword, ")
    you.do_you_have_wood_sword = True
    you.weapons.append("Gold Sword, ")
    you.do_you_have_gold_sword = True
    you.weapons.append("Silver Sword, ")
    you.do_you_have_silver_sword = True
    you.weapons.append("Diamond Sword, ")
    you.do_you_have_diamond_sword = True
    you.weapons.append("Enchanted Sword ")
    you.do_you_have_enchanted_sword = True
    print("You now have these weapons: %s" % "".join(you.weapons))
    you.damage = you.enchanted_sword_damage
input("Wait, I think I forgot my name")
input("Anyway, you have a mission")
input("Take back the world from the evil eldrazi")
input("For years they have been encased in stone waiting until they can take their revenge on this planet")
input("Now that the foolish humans have set them free")
input("The eldrazi might be able to destroy all life on this planet")
thing = input("What would you like to do")
if thing == "Skip1 Skip2 Skip3":
    you.skip_round_one = True
    you.skip_round_two = True
    you.did_you_beat_round_one = True
    you.did_you_beat_round_two = True
    you.did_you_get_to_the_mountain = True
    you.did_you_beat_the_mountain = True
elif thing == "Skip1 Skip2":
    you.skip_round_one = True
    you.skip_round_two = True
    you.did_you_beat_round_one = True
    you.did_you_beat_round_two = True
    you.did_you_get_to_the_mountain = True
elif thing == "Skip1":
    you.skip_round_one = True
    you.did_you_beat_round_one = True
elif thing == "Skip2":
    you.skip_round_two = True
    you.did_you_beat_round_two = True
elif thing == "Skip 3":
    you.did_you_beat_the_mountain = True
if thing == "Planeswalk":
    print("You went to another plane")
    print("Now you can relax")
    you.did_you_beat_round_one = True
    you.did_you_beat_round_two = True
    you.did_you_beat_the_entire_game = True
if thing == "19A":
    input("Mr. Wiebe: Your mom!")
    input("You just took ∞ damage")
    print("You died")
    print("Try again")
    you.did_you_lose_the_entire_game = True
if thing == "Ascend":
    you.did_you_beat_the_entire_game = True
    print("You have ascended")
    print("You fly above the world")
    print("In the far distance you see Ulamog")
    print("You speed toward at the speed of light")
    input("Suddenly")
    print()
    print()
    print()
    print()
    print()
    print()
    input("Out of nowhere")
    print()
    print()
    print()
    print()
    print()
    print()
    input("Comes")
    print()
    print()
    print()
    print()
    print()
    print()
    input("Kozilek")
    input("RRRRRrRRroeeeeoeoeoEEAOaoeoeRRrrrr")
    input("Kozilek swings one of his giant arms at you")
    input("You dodge effortlessly")
    input("Before he can react you swing your enchanted sword")
    input("BooooooOOoooOOoOooOooooOOMMMmmmMMmmMMMMmmmm")
    input("Anyone want sushi?")

while you.alive_round1 and not you.did_you_beat_round_one and not you.skip_round_one \
        and not you.did_you_beat_the_entire_game and not you.did_you_lose_the_entire_game:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print("".join(you.stuff), "".join(you.weapons), "".join(you.armors))
    elif beginning_choice == "2":
        you.map_item.append("Raven Gorge")
        print("".join(you.map_item[len(you.map_item) - 1]))
        print("Would you like to go to Raven Gorge?")
        decision2 = input("1: Yes 2: No")
        if decision2 == "1":
            print("You are now in Raven Gorge")
            print("An eldrazi scion has appeared")
            print("What would you like to do?")
            decision3 = input("1: Attack 2: Run")
            if decision3 == "2":
                print("The eldrazi killed you")
                print("Try again")
                you.alive_round1 = False
            while you.eldrazi_scion_health > 0:
                if decision3 == "1":
                    print("What would you like to attack with?")
                    decision4 = input("1: Stick")
                    if decision4 == "1":
                        you.eldrazi_scion_health -= 2
            if you.eldrazi_scion_health <= 0:
                print("You won")
                you.total_gold += 5
                print("You now have %s gold" % you.total_gold)
            print("Oh no! Now an eldrazi scion has appeared")
            print("What would you like to do?")
            decision5 = input("1: Fight 2: Run")
            if decision5 == "2":
                print("The eldrazi killed you")
                print("Try again")
                break
            while you.eldrazi_scout_health > 0 and not decision5 == "2" and you.total_health > 0:
                if decision5 == "1":
                    print("What would you like to attack with?")
                    decision6 = input("1: Stick")
                    if decision6 == "1":
                        you.eldrazi_scout_health -= 2
                    you.total_health -= you.eldrazi_scout_attack - you.armor
                if you.eldrazi_scout_health > 0:
                    print("The eldrazi scout now has %s health" % you.eldrazi_scout_health)
                else:
                    print("The eldrazi scout died")
                print("You have %s health left" % you.total_health)
            if you.eldrazi_scout_health <= 0:
                print("You won")
                you.total_gold += 10
                print("You now have %s gold" % you.total_gold)
            print("Would you like to look in the shop")
            decision7 = input("1: Yes 2: No")
            while decision7 == "1" and decision9 == "1" and not decision5 == "2":
                print("Healing Potion: 2 Gold")
                print("Wood Sword: 8 Gold")
                print("Wood Armor: 8 Gold")
                print("What would you like to buy?")
                decision8 = input("1: Healing Potion 2: Wood Sword 3: Wood Armor")
                if decision8 == "1" and you.total_gold >= 2:
                    you.total_health += 2
                    you.total_gold -= 2
                    print("Now you have %s health" % you.total_health)
                elif decision8 == "2" and you.total_gold >= 8:
                    damage = 4
                    you.total_gold -= 8
                    you.weapons.append("Wood sword,")
                    print("Now you deal 4 damage")
                elif decision8 == "3" and you.total_gold >= 8:
                    you.armor = 3
                    you.total_gold -= 8
                    print("Now you have 3 armor points")
                    you.armors.append("Wood armor,")
                elif decision8 == "4" and you.total_gold >= 1000000000000000000000000000000000:
                    did_you_beat_the_entire_game = True
                    you.total_gold -= 1000000000000000000000000000000000
                    input("You bought the mystery box")
                    input("You open the box")
                    input("Suddenly you get sucked inside")
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    you.did_you_beat_the_entire_game = True
                    input("You have won")
                    input("Congrats")
                    input("You used some cheats but bravo for finding them")
                    break
                print("You have %s gold left" % you.total_gold)
                print("Would you like to remain in the shop")
                decision9 = input("1: Yes 2: No")
            if not you.did_you_beat_the_entire_game:
                you.did_you_beat_round_one = True

if you.did_you_beat_round_one and not you.skip_round_one:
    print()
    print()
    print()
    print()
    g = input("So, this world is inhabited by the evil eldrazi and you need to save it")
    h = input("Ulamog is wreaking havoc all over this planet, Zendikar")
    i = input("If you do not act soon all of Zendikar will be destroyed")
    print("You got 20 gold for beating round 1")
    you.total_gold += 20
    print("Now you have %s gold" % you.total_gold)

you.map_item.append("Sheltered Valley")

while you.alive_round2 and not you.did_you_beat_round_two and not you.skip_round_two \
        and not you.did_you_beat_the_entire_game and not you.did_you_lose_the_entire_game:
    beginning_choice2 = input("1: Open inventory 2: Look at map")
    if beginning_choice2 == "1":
        print("".join(you.stuff), "".join(you.weapons), "".join(you.armors))
    elif beginning_choice2 == "2":
        print("".join(you.map_item[len(you.map_item)-1]))
        print("Would you like to go there?")
        dec1 = input("1: Yes 2: No")
        if dec1 == "1":
            print("You are now in Sheltered Valley")
            print("You see for the first time in a while that there is no destruction from the eldrazi")
            print("You see two paths, one going left and one going right")
            print("Which path would you like to follow?")
            dec2 = input("1: Left 2: Right")
            if dec2 == "1":
                print("You start heading down the left path")
                print("Suddenly in the distance you see a body")
                print("Do you want to walk towards it?")
                dec3 = input("1: Yes 2: No")
                if dec3 == "1":
                    print("You start walking towards the body and you soon see that there is blood all over it")
                    print("Although whoever it is spilt a lot of gold out of a bag")
                    you.total_gold += 50
                    print("You just got 50 gold")
                    print("Now you have %s gold" % you.total_gold)
                    print("You continue going down the path until you come to a stream")
                    print("You are very thirsty")
                    print("Do you take a drink of water?")
                    dec6 = input("1: Yes 2: No")
                    if dec6 == "1":
                        print("You take a long drink of the water and it tastes great")
                        print("You continue walking and slowly start feeling more and more dizzy")
                        print("Before you realize it your are on the ground and your eyes slowly start to close")
                        print("You died")
                        print("Try again")
                        you.alive_round2 = False
                    if dec6 == "2":
                        print("You decide not to take a drink of water because it might be unsanitary")
                        print("Ahead in the distance you begin to see what looks like a mountain")
                        you.did_you_beat_round_two = True
                        you.did_you_get_to_the_mountain = True
                    input("Poof")
                    input("A shop appears and it says")
                    input("Mountain shop: For all your mountain needs")
                    input("Would you like to go inside?")
                    you.dec9 = input("1: Yes 2: No")
                    while you.dec9 == "1" and dec12 == "1":
                        if you.dec9 == "1":
                            print("You are in the store")
                            print("This is what there is to buy")
                            print("Good Healing Potion: 5 Gold, Gold Sword: 10 Gold, Pickaxe: 10 Gold")
                            dec10 = input("1: Good Healing Potion 2: Gold Sword")
                            if dec10 == "1" and you.total_gold > 5:
                                you.total_gold -= 5
                                you.total_health += 5
                                print("You now have %s health" % you.total_health)
                                print("Now you have %s gold" % you.total_gold)
                            if dec10 == "2" and you.total_gold > 10 and not you.did_you_buy_gold_sword:
                                you.did_you_buy_the_gold_sword = True
                                you.total_gold -= 10
                                you.weapons.append("Gold Sword, ")
                                print("Now you have these weapons: %s" % "".join(you.weapons))
                                if you.gold_sword_damage > you.damage:
                                    damage = you.gold_sword_damage
                                    print("Now you do %s damage" % damage)
                                print("You have %s gold" % you.total_gold)
                            print("Would you like to remain in the shop")
                            dec12 = input("1: Yes 2: No")
                elif dec3 == "2":
                    print("You turned around and started walking the other way")
                    print("Suddenly, you hear a loud snap and see a flash of movement beside you")
                    dec4 = input("1: Investigate 2: Stay put")
                    if dec4 == "1":
                        print("You start walking towards the sound and realize there is a sword "
                              "sticking out of your chest")
                        print("You died")
                        print("Try again")
                        you.alive_round2 = False
                    if dec4 == "2":
                        print("The sound slowly fades away but whatever it is might come back")
                        print("You continue walking and before you know it the sun went down")
                        print("There are a lot of dry plants and sticks around you")
                        print("Do you want to make a fire?")
                        dec5 = input("1: Yes 2: No")
                        if dec5 == "1":
                            print("You make a small fire and before you know it you have fallen asleep")
                            print("When you wake up you check your surroundings, but nothing has changed")
                            print("You continue walking and soon the land becomes drier and drier")
                            print("Vegetation slowly starts to disappear and water appears to have flown away")
                            print("You find a sign that says, You have made it into the Great Desert, "
                                  "you are going to die")
                            you.did_you_beat_round_two = True
                            you.did_you_get_to_the_desert = True
                            input("Poof")
                            input("A shop appears and it says")
                            input("Desert shop: For all your desert needs")
                            input("Would you like to go inside")
                            dec11 = input("1: Yes 2: No")
                            while dec11 == "1" and dec13 == "1":
                                print("You are in the store")
                                print("This is what there is to buy")
                                print("Good Healing Potion: 5 Gold, Gold Sword: 10 Gold, Bottled Water: 5 Gold")
                                dec16 = input("1: Good Healing Potion 2: Gold Sword")
                                if dec16 == "1" and you.total_gold > 5:
                                    you.total_gold -= 5
                                    you.total_health += 5
                                    print("You now have %s health" % you.total_health)
                                    print("Now you have %s gold" % you.total_gold)
                                if dec16 == "2" and you.total_gold > 10 and not you.did_you_buy_gold_sword:
                                    did_you_buy_the_gold_sword = True
                                    you.total_gold -= 10
                                    you.weapons.append("Gold Sword, ")
                                    print("Now you have these weapons: %s" % "".join(you.weapons))
                                    if you.gold_sword_damage > you.damage:
                                        damage = you.gold_sword_damage
                                        print("Now you do %s damage" % damage)
                                    print("You have %s gold" % you.total_gold)
                                    if dec16 == "3" and you.total_gold > 5:
                                        you.total_gold -= 5
                                        print("You bought the bottled water")
                                print("Would you like to remain in the shop")
                                dec13 = input("1: Yes 2: No")
                        if dec5 == "2":
                            print("The sound you heard earlier starts to come back")
                            print("It gets louder and louder until it seems like it is completely surrounding you")
                            print("Suddenly 8 silhouettes come out of nowhere and 1 of them shoots you with a dart")
                            print("When you fall over you think it is a sleeping dart but you never end up waking up")
                            print("You died")
                            print("Try again")
                            you.alive_round2 = False
            elif dec2 == "2":
                print("You start heading down the right path")
                print("Up ahead you see a huge mess of trees")
                print("Do you want to go into the forest or keep walking along the edge of them")
                dec7 = input("1: Go into the forest 2: Walk along the edge")
                if dec7 == "2":
                    print("You decide not to go into the trees but to go along them")
                    print("You see what looks like a house in the distance but right as you are about to get "
                          "there an eldrazi appears and kills you before you can react")
                    print("You died")
                    print("Try again")
                    you.alive_round2 = False
                elif dec7 == "1":
                    print("You started walking into the forest")
                    print("Slowly, more and more light is being blocked by the trees")
                    print("Before you know it you are in almost complete darkness")
                    print("You begin to tire and wonder if you will ever make it out of the forest")
                    print("What do you want to do?")
                    dec8 = input("1: Stop and rest 2: Keep walking")
                    if dec8 == "1":
                        print("You find a smooth part of a tree and sit down with your back against it")
                        print("It seems to you like you are slowly being encased by the tree")
                        print("You are tired so you think nothing of it, but soon you get enveloped "
                              "and crushed by the tree")
                        print("You died")
                        print("Try again")
                        you.alive_round2 = False
                    elif dec8 == "2":
                        print("You keep walking for what seems like hours and you finally make it out of the trees")
                        print("Out in front of you is a vast lake that goes on farther than your eye can see")
                        you.did_you_get_to_the_lake = True
                        you.did_you_beat_round_two = True
                        input("Poof")
                        input("A shop appears and it says")
                        input("Lake shop: For all your lake needs")
                        print("Would you like to go inside?")
                        dec14 = input("1: Yes 2: No")
                        while dec14 == "1" and dec15 == "1":
                            print("You are in the store")
                            print("This is what there is to buy")
                            print("Good Healing Potion: 5 Gold, Gold Sword: 10 Gold, Boat: 20 Gold")
                            dec17 = input("1: Good Healing Potion 2: Gold Sword 3: Boat")
                            if dec17 == "1" and you.total_gold > 5:
                                you.total_gold -= 5
                                you.total_health += 5
                                print("You now have %s health" % you.total_health)
                                print("Now you have %s gold" % you.total_gold)
                            if dec17 == "2" and you.total_gold > 10 and not you.did_you_buy_gold_sword:
                                did_you_buy_the_gold_sword = True
                                you.total_gold -= 10
                                you.weapons.append("Gold Sword, ")
                                print("Now you have these weapons: %s" % "".join(you.weapons))
                                if you.gold_sword_damage > you.damage:
                                    you.damage = you.gold_sword_damage
                                    print("Now you do %s damage" % you.damage)
                                print("You have %s gold" % you.total_gold)
                            print("Would you like to remain in the shop")
                            dec15 = input("1: Yes 2: No")
                            if dec17 == "3" and you.total_gold >= 20:
                                print("Now you bought the boat")
                                print("You have %s gold left" % you.total_gold)
                                you.stuff.append("Boat")
                                you.do_you_have_the_boat = True

if you.did_you_beat_round_two:
    print("For beating round 2 you got 50 gold")
    you.total_gold += 50
    print("Now you have %s gold" % you.total_gold)

you.crab_thing_health = 10
you.crab_thing_attack = 3

while you.did_you_get_to_the_mountain and you.alive_in_the_mountain and not you.did_you_beat_the_entire_game \
        and not you.did_you_beat_the_mountain and not you.did_you_lose_the_entire_game:
    print()
    print()
    print()
    print()
    print()
    print("You are now near the mountain")
    print("There are 2 paths to climb the mountain")
    print("One leads to the left and it is very defined")
    print("The other leads to the left and is very faint")
    print("Which path would you like to take")
    mountain1 = input("1: Left 2: Right")
    if mountain1 == "2":
        print("You are on the path on the right")
        print("You start going higher up on the path")
        print("There is a strange button on the ground and you press it")
        input("Crreeeeaaeeeaeeaeeaeekkk")
        input("The ground moves away from under you and you free start to free fall")
        input("When you come to there are torches leading to your left and to your right")
        input("Do you want to go to the left or the right?")
        mountain7 = input("1: Left 2: Right")
        if mountain7 == "1":
            print("You start going left and the torches start to get brighter and brighter")
            input("Suddenly another trapdoor opens and this time you don't survive the fall")
            print("You died")
            print("Try again")
            you.alive_in_the_mountain = False
            you.did_you_lose_the_entire_game = True
        if mountain7 == "2":
            print("You start going to the right")
            input("Suddenly you are surrounded by strange creatures that are very pale")
            input("They start closing in on you and you have to act fast")
            input("Do you want to run or wave your sword at them")
            mountain8 = input("1: Run 2: Wave your sword")
            if mountain8 == "1" or mountain8 == "2":
                print("You run but some of the creatures grab your leg and you trip")
                input("Before you can get up you are being swarmed by the creatures")
                input("They grab your limbs and start carrying you down the dimly lit corridor")
                input("Suddenly the strange creatures drop you and run away")
                input("You start running the opposite way they were taking you but more creatures appear")
                input("This time they don't try to take you alive")
                input("Before you can even scream there are multiple swords in your stomach")
                print("You died")
                print("Try again")
                you.alive_in_the_mountain = False
                you.did_you_lose_the_entire_game = False
    elif mountain1 == "1":
        print("You are path on the left")
        print("This path is very well worn")
        print("You start walking and the sun starts to shine a lot")
        print("You can feel the sweat flowing down your face")
        print("As you get higher you start to have trouble breathing")
        print("You know you need to turn back or keep going")
        print("Do you want to turn back or keep going?")
        mountain2 = input("1: Turn back 2: Keep going")
        if mountain2 == "2":
            you.alive_in_the_mountain = False
            print("You start to feel light headed")
            print("All of a sudden it is hard to control your movements")
            print("You are spinning around and around in circles slowly getting closer to the edge of the mountain")
            print("You fell of the edge of the mountain")
            print("You died")
            print("Try again")
        elif mountain2 == "1":
            print("It becomes easier to breathe but you are still thirsty")
            print("Do you want to keep going or go back up")
            mountain3 = input("1: Keep going 2: Go back up")
            if mountain3 == "1":
                input("You continue going down the mountain")
                input("On your left is a cavern that you did not see when you came up")
                input("A clicking noise comes from it and")
                input("A")
                input("Crab thingy pops out")
                input("It has 4 legs and 2 ginormous pincers")
                input("It starts to swing its pincers at you")
                input("Do you want to parry or try to dodge")
                mountain4 = input("1: Parry 2: Dodge")
                while you.crab_thing_health > 0:
                    number_for_parry = random.randint(1, 4)
                    if mountain4 == "1":
                        if number_for_parry == 4:
                            print("You parried the crabs attack")
                        if not number_for_parry == 4:
                            print("The crab swung so hard he broke your %s" % you.weapons[0])
                            you.weapons.pop(0)
                    if mountain4 == "2":
                        number_for_dodge = random.randint(1, 4)
                        if number_for_dodge == 1:
                            print("You dodged the crab's attack")
                        if not number_for_dodge == 1:
                            damage_you_take_from_the_crab = you.crab_thing_attack - you.armor
                            print("The crab hit you straight in the chest and you took %s damage"
                                  % damage_you_take_from_the_crab)
                            you.total_health -= damage_you_take_from_the_crab
                            print("Now you have %s health" % you.total_health)
                    print("Do you want to attack or flee")
                    mountain5 = input("1: Attack 2: Flee")
                    if mountain5 == "1":
                        print("You have these weapons: %s" % "".join(you.weapons))
                        mountain_bronze = input("1: %s 2: %s" %
                                                (you.weapons[len(you.weapons) - 2], you.weapons[len(you.weapons) - 1]))
                        if mountain_bronze == "1" or mountain_bronze == "2":
                            you.crab_thing_health -= you.damage
                        if you.crab_thing_health > 0:
                            print("The crab thingy now has %s health left" % you.crab_thing_health)
                            you.total_health -= you.crab_thing_attack
                        else:
                            print("The crab thingy now has 0 health left")
                            print("You won!")
                            you.total_gold += 15
                            print("Now you have %s gold" % you.total_gold)
                        print("You now have %s health" % you.total_health)
                    if mountain5 == "2" or you.crab_thing_health < 0:
                        did_you_find_the_cave = random.randint(1, 4)
                        if did_you_find_the_cave == 1:
                            print("Suddenly there is a rumble and you part of the mountain beside you moves away "
                                  "showing a dimly lit passage leading down")
                            print("Do you want to enter the cave?")
                            mountain6 = input("1: Enter the cave 2: Keep going")
                            if mountain6 == "1":
                                print("You slowly entered the cave")
                                you.did_you_get_to_the_cave = True
                                you.did_you_beat_the_mountain = True
                        if not did_you_find_the_cave == 1:
                            print("You stumbled over a pebble and fell to your death")
                            you.did_you_lose_the_entire_game = False
                            you.alive_in_the_mountain = False

while you.did_you_get_to_the_cave and you.alive_in_the_cave and not you.did_you_beat_the_entire_game \
        and not you.did_you_lose_the_entire_game and not you.did_you_beat_the_cave:
    input("You are now in the cave")
    input("You look around and there are torches mounted along the wall leading to the left and to the right")
    print("Which way do you want to go")
    cave1 = input("1: Left 2: Right")
    if cave1 == "1":
        input("You start heading to the left")
        input("Slowly the lights start to get dimmer")
        input("Do you want to keep going to the left or go back to where you fell")
        cave2 = input("1: Keep going 2: Go back")
        if cave2 == "1":
            print("You keep going")
            input("Soon there are no torches lighting your path and you can't see anything")
            input("Suddenly in the distance a dim light appears")
            input("You start heading towards the light but then you hear a voice")
            input("My precious")
            input("Guide my broken hands")
            input("Show them where to strike")
            input("You start to hear a patter of feet that is steadily getting louder")
            input("You start to run but the footsteps keep getting louder")
            input("You turn around and whatever is chasing you is right behind you")
            input("You feel a prick in your back and then a sharp object gets plunged through your chest")
            input("You look up to see a shadow standing over you")
            input("My precious")
            input("We shall feast well tonight")
            you.alive_in_the_cave = False
            you.did_you_lose_the_entire_game = False
    # Implement the pick axe
    # When done set did_you_get_to_the_cave back to false

while you.did_you_get_to_the_desert and you.alive_in_the_desert and not you.did_you_beat_the_entire_game \
        and not you.did_you_beat_the_desert and not you.did_you_lose_the_entire_game:
    print("You are now in the desert")
while you.did_you_get_to_the_lake and you.alive_in_the_lake and not you.did_you_beat_the_entire_game\
        and not you.did_you_beat_the_lake and not you.did_you_lose_the_entire_game:
    print("You are now by the lake")
