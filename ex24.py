print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and\ttabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuision
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------------------------------------")
print(poem)
print("-----------------------------------------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
print("\n")

def secret_formular(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#beans, jars, crates = secret_formular(start_point)
x, y, z = secret_formular(start_point)

#remeber that this is another way to format a string
print("With a starting point of: {}".format(start_point))

#Its just like with an f"" string
print(f"We'd have {x} beans, {y} jars, and {z} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formular = secret_formular(start_point)

#This is another way
#m, n, o = secret_formular(start_point)
#print("we'd have {} beans, {} jars, and {} crates.".format(m , n , o))

#This is an easy way to apply a list to a format starting
#The asterik before the formular is to tell pytho n that we are parsing in more than one variable and that it should take all.
print("we'd have {} beans, {} jars, and {} crates.".format(*formular))
