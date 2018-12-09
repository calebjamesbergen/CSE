import random
stuff = ["Map, "]
weapons = ["Stick, "]
armors = ["Leather armor, "]
stick_damage = 1
do_you_have_stick = True
bronze_sword_damage = 3
buy_bronze_sword = False
do_you_have_bronze_sword = False
gold_sword_damage = 5
buy_gold_sword = False
do_you_have_gold_sword = False
silver_sword_damage = 10
buy_silver_sword = False
do_you_have_silver_sword = False
diamond_sword_damage = 15
do_you_have_diamond_sword = False
enchanted_sword_damage = 20
do_you_have_enchanted_sword = False
leather_armor_defence = 1
do_you_have_leather_armor = True
mail_armor_defence = 5
do_you_have_mail_armor = False
silver_armor_defence = 10
do_you_have_silver_armor = False
enchanted_armor_defence = 20
do_you_have_enchanted_armor = False
damage = stick_damage
armor = leather_armor_defence
total_health = 5
total_gold = 0
eldrazi_scion_health = 1
eldrazi_scion_attack = 0
eldrazi_scout_health = 5
eldrazi_scout_attack = 2
decision9 = "1"
dec12 = "1"
alive_round1 = True
alive_round2 = True
did_you_beat_round_one = False
did_you_beat_round_two = False
skip_round_one = False
skip_round_two = False
did_you_beat_the_entire_game = False
did_you_lose_the_entire_game = False
map_item = []


input("Press enter to scroll through dialogue")
b = input("Hello human")
if b == "Give me the money":
    total_gold += 1000000000000000000000000000000000
    print("You found it")
    print("You now have %s gold" % total_gold)
c = input("It is I")
if c == "Give me the money":
    total_gold -= 1000000000000000000000000000000000
    print("Ha, you failed")
    print("Now you have %s gold" % total_gold)
input("The all knowing")
print()
print()
print()
d = input()
if d == "Armor":
    armors.append("Mail Armor, ")
    do_you_have_mail_armor = True
    armors.append("Silver Armor, ")
    do_you_have_silver_armor = True
    armors.append("Enchanted Armor")
    do_you_have_enchanted_armor = True
    armor = enchanted_armor_defence
    print("Now you have these armors: %s" % "".join(armors))
input("Powerful")
print()
print()
print()
e = input()
if e == "Weapons":
    weapons.append("Wood Sword, ")
    do_you_have_wood_sword = True
    weapons.append("Gold Sword, ")
    do_you_have_gold_sword = True
    weapons.append("Silver Sword, ")
    do_you_have_silver_sword = True
    weapons.append("Diamond Sword, ")
    do_you_have_diamond_sword = True
    weapons.append("Enchanted Sword ")
    do_you_have_enchanted_sword = True
    print("You now have these weapons: %s" % "".join(weapons))
    damage = enchanted_sword_damage
input("Wait, I think I forgot my name")
input("Anyway, you have a mission")
input("Take back the world from the evil eldrazi")
input("For years they have been encased in stone waiting until they can take their revenge on this planet")
input("Now that the foolish humans have set them free")
input("The eldrazi might be able to destroy all life on this planet")
thing = input("What would you like to do")
if thing == "Skip1 Skip2":
    skip_round_one = True
    skip_round_two = True
    did_you_beat_round_one = True
    did_you_beat_round_two = True
elif thing == "Skip1":
    skip_round_one = True
    did_you_beat_round_one = True
elif thing == "Skip2":
    skip_round_two = True
    did_you_beat_round_two = True
if thing == "Planeswalk":
    print("You went to another plane")
    print("Now you can relax")
    did_you_beat_round_one = True
    did_you_beat_round_two = True
    did_you_beat_the_entire_game = True
if thing == "19A":
    input("Mr. Wiebe: Your mom!")
    input("You just took ∞ damage")
    print("You died")
    print("Try again")
    did_you_lose_the_entire_game = True
if thing == "Ascend":
    did_you_beat_the_entire_game = True
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

while alive_round1 and not did_you_beat_round_one and not skip_round_one and not did_you_beat_the_entire_game \
        and not did_you_lose_the_entire_game:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print("".join(stuff), "".join(weapons), "".join(armors))
    elif beginning_choice == "2":
        map_item.append("Raven Gorge")
        print("".join(map_item[len(map_item) - 1]))
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
                alive_round1 = False
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
            print("Oh no! Now an eldrazi scion has appeared")
            print("What would you like to do?")
            decision5 = input("1: Fight 2: Run")
            if decision5 == "2":
                print("The eldrazi killed you")
                print("Try again")
                break
            while eldrazi_scout_health > 0 and not decision5 == "2" and total_health > 0:
                if decision5 == "1":
                    print("What would you like to attack with?")
                    decision6 = input("1: Stick")
                    if decision6 == "1":
                        eldrazi_scout_health -= 2
                total_health -= eldrazi_scout_attack - armor
                if eldrazi_scout_health > 0:
                    print("The eldrazi scout now has %s health" % eldrazi_scout_health)
                else:
                    print("The eldrazi scout died")
                print("You have %s health left" % total_health)
            if eldrazi_scout_health <= 0:
                print("You won")
                total_gold += 10
                print("You now have %s gold" % total_gold)
            print("Would you like to look in the shop")
            decision7 = input("1: Yes 2: No")
            while decision7 == "1" and decision9 == "1" and not decision5 == "2":
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
                    weapons.append("Wood sword,")
                    print("Now you deal 4 damage")
                elif decision8 == "3" and total_gold >= 8:
                    armor = 3
                    total_gold -= 8
                    print("Now you have 3 armor points")
                    armors.append("Wood armor,")
                elif decision8 == "4" and total_gold >= 1000000000000000000000000000000000:
                    did_you_beat_the_entire_game = True
                    total_gold -= 1000000000000000000000000000000000
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
                    input("You have won")
                    input("Congrats")
                    input("You used some cheats but bravo for finding them")
                    break
                print("You have %s gold left" % total_gold)
                print("Would you like to remain in the shop")
                decision9 = input("1: Yes 2: No")
            if not did_you_beat_the_entire_game:
                did_you_beat_round_one = True

if did_you_beat_round_one and not skip_round_one:
    print()
    print()
    print()
    print()
    g = input("So, this world is inhabited by the evil eldrazi and you need to save it")
    h = input("Ulamog is wreaking havoc all over this planet, Zendikar")
    i = input("If you do not act soon all of Zendikar will be destroyed")
    # alive_round2 = False

did_you_beat_round_two = False
did_you_get_to_the_mountain = False
did_you_get_to_the_desert = False
did_you_get_to_the_lake = False

map_item.append("Sheltered Valley")

while alive_round2 and not did_you_beat_round_two and not skip_round_two and not did_you_beat_the_entire_game \
        and not did_you_lose_the_entire_game:
    beginning_choice2 = input("1: Open inventory 2: Look at map")
    if beginning_choice2 == "1":
        print("".join(stuff), "".join(weapons), "".join(armors))
    elif beginning_choice2 == "2":
        print("".join(map_item[len(map_item)-1]))
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
                    total_gold += 50
                    print("You just got 50 gold")
                    print("Now you have %s gold" % total_gold)
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
                        alive_round2 = False
                    if dec6 == "2":
                        print("You decide not to take a drink of water because it might be unsanitary")
                        print("Ahead in the distance you begin to see what looks like a mountain")
                        did_you_beat_round_two = True
                        did_you_get_to_the_mountain = True
                    input("Poof")
                    input("A shop appears and it says")
                    input("Mountain shop: For all your mountain needs")
                    input("Would you like to go inside?")
                    dec9 = input("1: Yes 2: No")
                    while dec9 == "1" and dec12 == "1":
                        if dec9 == "1":
                            print("You are in the store")
                            print("This is what there is to buy")
                            print("Good healing Potion: 5 Gold Gold Sword: 10 Gold")
                            dec10 = input("1: Good Healing Potion 2: Gold Sword")
                            if dec10 == "1" and total_gold > 5:
                                total_gold -= 5
                                total_health += 5
                                print("You now have %s health" % total_health)
                                print("Now you have %s gold" % total_gold)
                            if dec10 == "2" and total_gold > 10 and not did_you_buy_the_gold_sword:
                                did_you_buy_the_gold_sword = True
                                total_gold -= 10
                                weapons.append("Gold Sword, ")
                                print("Now you have these weapons: %s" % "".join(weapons))
                                if gold_sword_damage > damage:
                                    damage = gold_sword_damage
                                    print("Now you do %s damage" % damage)
                                    print("You have %s gold" % total_gold) 
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
                        alive_round2 = False
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
                            did_you_beat_round_two = True
                            did_you_get_to_the_desert = True
                            input("Poof")
                            input("A shop appears and it says")
                            input("Desert shop: For all your desert needs")
                            input("Would you like to go inside")
                            dec11 = input("1: Yes 2: No")
                        if dec5 == "2":
                            print("The sound you heard earlier starts to come back")
                            print("It gets louder and louder until it seems like it is completely surrounding you")
                            print("Suddenly 8 silhouettes come out of nowhere and 1 of them shoots you with a dart")
                            print("When you fall over you think it is a sleeping dart but you never end up waking up")
                            print("You died")
                            print("Try again")
                            alive_round2 = False
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
                    alive_round2 = False
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
                        alive_round2 = False
                    elif dec8 == "2":
                        print("You keep walking for what seems like hours and you finally make it out of the trees")
                        print("Out in front of you is a vast lake that goes on farther than your eye can see")
                        did_you_get_to_the_lake = True
                        did_you_beat_round_two = True
                        input("Poof")
                        input("A shop appears and it says")
                        input("Lake shop: For all your lake needs")

alive_in_the_mountain = True
alive_in_the_lake = True
alive_in_the_desert = True

did_you_get_to_the_mountain = True
did_you_get_to_the_desert = False
did_you_get_to_the_lake = False

did_you_beat_the_mountain = False
did_you_beat_the_lake = False
did_you_beat_the_desert = False

crab_thing_health = 10
crab_thing_attack = 3

while did_you_get_to_the_mountain and alive_in_the_mountain and not did_you_beat_the_entire_game \
        and not did_you_beat_the_mountain and not did_you_lose_the_entire_game:
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
    if mountain1 == "1":
        print("You are path on the right")
        print("This path is very well worn")
        print("You start walking and the sun starts to shine a lot")
        print("You can feel the sweat flowing down your face")
        print("As you get higher you start to have trouble breathing")
        print("You know you need to turn back or keep going")
        print("Do you want to turn back or keep going?")
        mountain2 = input("1: Turn back 2: Keep going")
        if mountain2 == "2":
            alive_in_the_mountain = False
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
                while crab_thing_health > 0:
                    number = random.randint(1, 4)
                    if mountain4 == "1":
                        if number == 4:
                            print("You parried the crabs attack")
                        if not number == 4:
                            print("The crab swung so hard he broke your %s" % weapons[0])
                            weapons.pop(0)
                        print("Do you want to attack or flee")
                        mountain5 = input("1: Attack 2: Flee")
                        if mountain5 == "1":
                            print("You have these weapons: %s" % "".join(weapons))
                            mountain_bronze = input("1: %s 2: %s" %
                                                    (weapons[len(weapons) - 2], weapons[len(weapons) - 1]))
                            if mountain_bronze == "1" or mountain_bronze == "2":
                                crab_thing_health -= damage
                            if crab_thing_health > 0:
                                print("The crab thingy now has %s health left" % crab_thing_health)
                                total_health -= crab_thing_attack
                            else:
                                print("The crab thingy now has 0 health left")
                                print("You won!")
                                total_gold += 15
                                print("Now you have %s gold" % total_gold)
                            print("You now have %s health" % total_health)

while did_you_get_to_the_desert and alive_in_the_desert and not did_you_beat_the_entire_game \
        and not did_you_beat_the_desert and not did_you_lose_the_entire_game:
    print("You are now in the desert")
while did_you_get_to_the_lake and alive_in_the_lake and not did_you_beat_the_entire_game\
        and not did_you_beat_the_lake and not did_you_lose_the_entire_game:
    print("You are now by the lake")
