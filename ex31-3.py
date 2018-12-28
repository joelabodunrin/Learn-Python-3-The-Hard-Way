print("\n")
print("Give me a whole number between 1 and 50 and I will tell you if its even number or odd number.")
print("\n")

x_x = input("Enter the number here: >>  "   )
x = int(x_x)

if 1 <= x and x <= 50 and x % 2 == 0:
    print(f"The number you entered is '{x}' and it's between 1 and 50")
    print(f"{x} an EVEN NUMBER.")
elif 1 <= x and x <=50 and x % 2 != 0:
    print(f"The number you entered is '{x}' and it's between 1 and 50")
    print(f"{x} is an ODD NUMBER")
elif 1 > x or x > 50:
    print("The number is either less than 1 or greater than 50")
else:
    print("Enter whole number between 1 and 50.")
