name = 'Abodunrin E. Joel'
age = 32 #not a lie
height_in_inches = 78 # I am not sure
height_in_meters = height_in_inches / 39.37
weight_in_kg = 79 #Kg. Not very sure #too
weight_in_pounds = weight_in_kg * 2.20462
eyes = 'Blue'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height_in_inches} inches tall and {height_in_meters} meters tall if you talk in meters.")
print(f"He's {weight_in_kg} kilogram heavy and {weight_in_pounds} pounds heavy if you talk in pounds.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_in_inches + weight_in_pounds
print(f"If I add {age}, {height_in_inches}, and {weight_in_pounds} I get {total}.")
