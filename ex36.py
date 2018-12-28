#Ask a question
#if its right assign 5 marks and move on to another question.
#If wrong return no mark and give another chamce
#else dead
from sys import exit

def question_1():
    print("Let's play a little game.")
    print("What is the capital city of Madagascar?")
    name = input("> " )

    if "Antananarivo" in name:
        point_tracker("Good start!,", 5)
        question_2()
    elif "Antananarivo" not in name:
        print("Wrong, you have another chance")
        print("Also make sure you capitalize the first alphabelt next time")
        question_1_alt()
    else:
        print("You can't be that daft!")
        dead()

def question_1_alt():
    print("Make good use of this chance, could be the last.")
    print("Here is the question.")
    print("What is the capital of Namibia?")
    name_alt = input("> " )

    if "Windhoek" in name_alt:
        point_tracker("NIce attempt this time,", 5)
        question_2()
    elif "Windhoek" not in name_alt:
        print("You wasted your second chance.")
        dead()
    else:
        print("What am I suppose to do with you.")


#Ask another question for those right with question_1
#Same goes for those who pass question_1_alt
#if correct, add 5 marks
#if wrong subtract the 5 marks earlier gotten and return to comment 3
#else dead
def question_2():
    print("Here is your second question")
    print("Which country is tripolitania part of?")
    answer = input("> " )

    if "Libya" in answer :
        point_tracker("Thats impressive, keep up the good work,", 10)
        question_3()
    elif "Libya" not in answer:
        print("Awww! That's wrong")
        point_tracker("Although you have another chance but your 5 point has been deducted,", 0)
        print("Also make sure you capitalize the first alphabelt next time")
        question_1_alt()
    else:
        print("You are smarter than that.")
        dead()



#if correct from above, ask the last question.
#if correct, print you are a champion (20/20)
#if wrong end (your total score is ...)
#else dead
def question_3():
    print("You are almost there, THE GENIUS")
    print("Here is your last question")
    print("Which country was fromerly named 'Rhodesia'")
    country = input("> " )

    if "Zimbabwe" in country:
        print("BOY! YOU ARE A GENIUS")
        print("or may be you sought help from Google")
        print("Nevertheless, you are smart")
        print("You are a champ, 15/15")
        dead()
    elif "Zimbabwe" not in country:
        print("Oh! you missed that one.")
        print("Your total score is 10/15")
    else:
        print("Like seriously, you need help")

#if wrong from line 3, you wasted your second chance
#else dead
#if right go through the process again



def point_tracker(comment, point):
    x = int(point) + int(0)
    print(comment, f"{x} point for you.")

def dead():
    exit(0)

question_1()
