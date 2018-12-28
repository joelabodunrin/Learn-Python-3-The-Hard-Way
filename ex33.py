def add_to_list():
    #i = 0
    x = int(input("Enter the fisrt number in the list >> " ))
    y = int(input("Enter the last number in the list >> " ))
    z = int(input("Enter Increment >> " ))

    numbers = []

    while x < y:
        print(f"At the top start is {x}")
        numbers.append(x)

        x = x + z
        print("Numbers now: ", numbers)
        print(f"At the bottom start is {x}")


    print("The numbers: ")

    for num in numbers:
        print(num)

add_to_list()
