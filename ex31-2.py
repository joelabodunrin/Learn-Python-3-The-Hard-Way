print("This is a game on how to get to my house from office.")
print("\n")
print("From Akin-Olugbade, You either take bike to costain or board bus.")
print("""Choose 1 to take bike or 2 to board bus.""")

option = input("> " )

if option == "1":
    print("You will get to Costain in approx. 35 minutes.")
    print("I think you made the right choice.")
    print("When you get to Costain, you could Take bike or board NAPEP")
    print("So what will it be?")
    print("""1. Take bike
             2. Board NAPEP""")

    option_2 = input("> " )
    if option_2 == "1":
        print("You are taking bike too much, It's not safe.")
        print("However, Its still the fastest option")
    elif option_2 == "2":
        print("It's the safest option but you could be delayed due to trafic")
        print("On normal days, I will prefer this.")
    else:
        print("Its either you trek or sleep under costain bridge.")
        print("Shimple, END!")

elif option == "2":
    print("You will spend 2 hours to costain if traffic smile on you.")
    print("You could regret your choice.")
    print("""By the time yo get to costain tired and haggard,
             you have two options. So what will it be?""")
    print("""1. Take bike
             2. Board NAPEP""")

    option_3 = input("> " )

    if option_3 == "1":
        print("I understand you are tired and you want to get home fast.")
        print("But this could be a wrong choice as its not safe.")
        print("But if you are lucky, no accident, you will get home on time.")

    elif option_3 == "2":
        print("Its better to be saafe I guess.")
        print("This is the safest option, although you could get home late.")

    else:
        print("With that option, its obvious you want to sleep under costain bridgr")
