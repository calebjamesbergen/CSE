# Do not forgot to compare responses to "1" not just 1
inventory = ["Stick,", "Leather armor,",  "Map,"]
damage = 1
armor = 1
total_health = 5
total_gold = 0
eldrazi_scion_health = 1
eldrazi_scion_attack = 0
eldrazi_scout_health = 5
eldrazi_scout_attack = 2
decision9 = "1"
alive_round1 = True
alive_round2 = True
did_you_beat_round_one = False
did_you_beat_round_two = False
skip_round_one = False
skip_round_two = False
did_you_beat_the_entire_game = False
map_item = []


a = input("Press enter to scroll through dialogue")
b = input("Hello human")
if b == "Give me the money":
    total_gold += 10000000000000
    print("You found it")
    print("You now have %s gold" % total_gold)
c = input("It is I")
if c == "Give me the money":
    total_gold -= 10000000000000
    print("Ha, you failed")
    print("Now you have %s gold" % total_gold)
d = input("The all knowing")
print()
print()
print()
print()
e = input("Powerful")
print()
print()
print()
print()
f = input("Wait, I think I forgot my name")
g = input("Anyway, you have a mission")
h = input("Take back the world from the evil eldrazi")
i = input("For years they have been encased in stone waiting until they can take their revenge on this planet")
j = input("Now that the foolish humans have set them free")
k = input("The eldrazi might be able to destroy all life on this planet")
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
if thing == "Ascend":
    print("You have ascended")
    print("You fly above the world")
    print("In the far distance you see Ulamog")
    print("You speed toward at the speed of light")
    m = input("Suddenly")
    print()
    print()
    print()
    print()
    print()
    print()
    n = input("Out of nowhere")
    print()
    print()
    print()
    print()
    print()
    print()
    o = input("Comes")
    print()
    print()
    print()
    print()
    print()
    print()
    p = input("Kozilek")
    q = input("RRRRRrRRroeeeeoeoeoEEAOaoeoeRRrrrr")
    r = input("Kozilek swings one of his giant arms at you")
    s = input("You dodge effortlessly")
    t = input("Before he can react you swing your enchanted sword")
    u = input("BooooooOOoooOOoOooOooooOOMMMmmmMMmmMMMMmmmm")
    v = input("Anyone want sushi?")


while alive_round1 and not did_you_beat_round_one and not skip_round_one and not did_you_beat_the_entire_game:
    beginning_choice = input("1: Open inventory 2: Look at map")
    if beginning_choice == "1":
        print(*inventory, sep=" ")
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
                print("The eldrazi scout now has %s health" % eldrazi_scout_health)
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
                    inventory.append("Wood sword,")
                    print("Now you deal 4 damage")
                elif decision8 == "3" and total_gold >= 8:
                    armor = 3
                    total_gold -= 8
                    print("Now you have 3 armor points")
                    inventory.append("Wood armor,")
                print("You have %s gold left" % total_gold)
                print("Would you like to remain in the shop")
                decision9 = input("1: Yes 2: No")
            did_you_beat_round_one = True

if did_you_beat_round_one:
    print()
    print()
    print()
    print()
    g = input("So, this world is inhabited by the evil eldrazi and you need to save it")
    h = input("Ulamog is wreaking havoc all over this planet, Zendikar")
    i = input("If you do not act soon all of Zendikar will be destroyed")
else:
    print("You died")
    # alive_round2 = False

did_you_beat_round_two = False
did_you_get_to_the_mountain = False
did_you_get_to_the_desert = False
did_you_get_to_the_lake = False

map_item.append("Sheltered Valley")

while alive_round2 and not did_you_beat_round_two and not skip_round_two and not did_you_beat_the_entire_game:
    beginning_choice2 = input("1: Open inventory 2: Look at map")
    if beginning_choice2 == "1":
        print(*inventory, sep=" ")
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
        and not did_you_beat_the_mountain:
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
            print("Do you want to keep going or turn back")
            mountain3 = input("1: Keep going 2: Turn back")


while did_you_get_to_the_desert and alive_in_the_desert and not did_you_beat_the_entire_game \
        and not did_you_beat_the_desert:
    print("You are now in the desert")
while did_you_get_to_the_lake and alive_in_the_lake and not did_you_beat_the_entire_game\
        and not did_you_beat_the_lake:
    print("You are now by the lake")
