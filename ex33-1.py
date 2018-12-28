#This is to use for-loop to achieve excercise 33 where while loop was used. 

elements = []

x = int(input("Enter the fisrt number in the list >> " ))
y = int(input("Enter the last number in the list >> " ))
z = int(input("Enter Increment >> " ))

for i in range(x, y, z):
    elements.append(i)
for i in elements:
    print(i)
