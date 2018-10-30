while 0 == 0:
    answer = ""
    import random
    for x in range(1):
        x = random.randint(1, 5)
    if x == 1:
        answer = "Yes"
    if x == 2:
        answer = "No"
    if x == 3:
        answer = "Maybe"
    if x == 4:
        answer = "As likely as ice cream raining from the sky"
    if x == 5:
        answer = "As likely as Donald Trump being reelected for president"
    question = input("Ask me a yes or no question ")
    print("%s" % answer)
