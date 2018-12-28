#This prints the string and the input below grasp something from the user to store as a variable
#end ' ' as seen in others is to make sure that the input is gotten right infront of the question and not on the next line
#Run the program and see the difference between line 4 and line 6
print("How old are you?" )
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Another way of writing the same code
x = input("How old are you?: " )
y = input("How tall are you?: ")
z = input("How much do you weigh?: ")

print(f"So, you're {x} old, {y} tall and {z} heavy.")

print("""I can solve the equation below for you
         x*2 + y*3 + x*y + x*y*z / z*3 - x*y
         Supply the value of x,y and z.
         """)
print("What's your value of x?")
x = int(input())
print("What's your value of y?")
y = int(input())
print("What's your value of z?")
z = int(input())
eqn = x*2 + y**3 + x*y + x*y*z / z*3 - x*y
print("Your answer is: ", eqn)

#print(f"{x} is my name")
#print("My name is", x)
