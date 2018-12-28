#import from library
from sys import argv
script, filename = argv

#print some strings
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#print the strin and take an input
input("?")

#print the string
print("Opening the file...")

#parse into a variable and open
target = open(filename, 'w')

#deleting the file
print("Truncating the file. Goodbye!")
target.truncate()

#print string
print("Now I'm going to ask you for three lines.")

#enter values to be written into a file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#print a string
print("I'm going to write these to the file.")

#write to file
target.write(f"{line1} \n{line2} \n{line3}" )
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()
