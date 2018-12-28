#Here is some new strange stuff, remember type it correctly

#Assign variables to a string
days = "Mon Tue Wed Thu Fri Sat Sun"
#Assign variables to a string but we want it printed across multiple line.
#can also be achieved with line 18 i.e tripple quote
months = "Jan\nFeb\nMar\nApr\nApr\nMay\nJun\nJul\nAug"

#Print to terminal with an arguement parsed in
print("Here are the days: ", days)
#This is another way of writing line 10
print(f"Here are the days: {days}")
print("Here are the months: ", months)

#I guess it's for printing long strings, not sure though.
#If you use 3 double quotes, you can also have quotes in your
#string and python won't confuse it.
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much "Say for example"as we like.
Even 4 lines if we want, or 5, or 6.
""")
