from sys import argv

script, user_name, username = argv
prompt = '>>>>>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")

#from sys import argv

#script, username = argv
#prompt = '> '

print(f"Hi {username}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {username}?")
likes1 = input()

print(f"Where do you live {username}?")
lives1 = input()

print("What kind of computer do you have?")
computer1 = input()

print(f"""
Alright, so you said {likes1} about liking me.
You live in {lives1}. Not sure where that is.
And you have a {computer1} computer. Nice
""")
