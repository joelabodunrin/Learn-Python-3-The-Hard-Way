formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Trying my own",
        "Eager to see what this will do",
        "I am going to try my hand on poem someday",
        "Because I have no fear"
))
