#Defibe the function and gives it two arg
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print some strings and parsed in arg
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#Its like pressing enter to have a line
print("\n")
#print string
print("We can just give the function numbers directly:")
#run/call the function with the two arg provided
cheese_and_crackers(20, 30)


#This part does the same thing but assign the arg to variable first
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This part does the same thing but did maths with the arg
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Did the same thing but did math involving numbers and earlier creayed variable
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
