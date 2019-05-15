import random


def rock_paper_scissors():
    lives = 3
    times_you_have_won = 0

    print("This is rock paper scissors")
    print("To choose what to do either type 'rock' 'paper' or 'scissors")
    print("What do you choose?")

    while lives > 0:
        thing1 = input(">_")

        dice_roll = random.randint(1, 3)
        thing2 = ""

        if dice_roll == 1:
            thing2 = "rock"

        if dice_roll == 2:
            thing2 = "paper"

        if dice_roll == 3:
            thing2 = "scissors"

        if thing1 == "rock":
            print()
            if thing2 == "rock":
                print("Your opponent did rock")
                print("Nothing happened")
            if thing2 == "paper":
                print("Your opponent did paper")
                print("You lost")
                lives -= 1
                print("Now you have %s lives left" % lives)
            if thing2 == "scissors":
                print("Your opponent did scissors")
                print("You won")
                times_you_have_won += 1
                print("You have won %s times" % times_you_have_won)
                lives += 1
                print("You got 1 additional live\nNow you have %s lives" % lives)

        if thing1 == "paper":
            print()
            if thing2 == "rock":
                print("Your opponent did rock")
                print("You won")
                times_you_have_won += 1
                print("You have won %s times" % times_you_have_won)
                print("You have won %s times" % times_you_have_won)
                lives += 1
                print("You got 1 additional live\nNow you have %s lives" % lives)
            if thing2 == "paper":
                print("Your opponent did rock")
                print("Nothing happened")
            if thing2 == "scissors":
                print("Your opponent did scissors")
                print("You lost")
                lives -= 1
                print("Now you have %s lives left" % lives)

        if thing1 == "scissors":
            print()
            if thing2 == "rock":
                print("Your opponent did rock")
                print("You lost")
                lives -= 1
                print("Now you have %s lives left" % lives)
            if thing2 == "paper":
                print("Your opponent did paper")
                print("You won")
                times_you_have_won += 1
                print("You have won %s times" % times_you_have_won)
                lives += 1
                print("You got 1 additional live\nNow you have %s lives" % lives)
                print("You have won %s times" % times_you_have_won)
            if thing2 == "scissors":
                print("Your opponent did rock")
                print("Nothing happened")
