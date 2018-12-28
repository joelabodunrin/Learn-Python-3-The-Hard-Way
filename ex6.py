#Assigning a variable
types_of_people = 10
#Assigning another variable but parsing in another variable
x = f"There are {types_of_people} types of people."

#Assigning a varibale
binary = "binary"
do_not = "don't"
#Assigning another variable and parsing in two variables
y = f"Those who know {binary} and those who {do_not}."

#Print to terminal
print(x)
print(y)

#print to terminal parsing in two variables
print(f"I said: {x} ")
print(f"I also said: '{y}' ")

#Assigning a variable
hilarious = False
#Assigning a variable and leaving space for format in next code
joke_evaluation = "Isn't that joke so funny?! {}"

#print to terminal parsing in hilarious
print(joke_evaluation.format(hilarious))

#Assigning a variable
w = "This is the left side of..."
e = "a string with a right side."

#Joining two strings using plus
print(w + e)






# Python3 program to demonstarte
# the str.format() method

# using format option in a simple string
print ("{}, A computer science portal for geeks."
                        .format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print (str.format("Python"))

# formatting a string using a numeric constant
print ("Hello, I am {} years old !".format(18))
