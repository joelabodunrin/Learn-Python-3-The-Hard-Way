#Import modules
from sys import argv
#Needed arguement variable
script, filename = argv
#Open the file and store in a variable
txt = open(filename)
#print something to terminal
print(f"Here's your file {filename}:")
#print the file already captured into a variable
print(txt.read())

#another way of doing it
print("Type the filename again:")
#To capture the file name in a varible and also print <>
file_again = input("<> ")
#To open from the varible and store in another variable
txt_again = open(file_again)
#print to terminal
print(txt_again.read())
