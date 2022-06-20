print("Welcome to my CSGO quizz!")

play_game = input("Do you want to play the game? ")

if play_game.lower() != "yes":
    quit()

print("Lets play!! :)")

score = 0
total_questions = 0

answer = input("Which pistol costs 700$? ")
total_questions += 1
if answer.lower() == "desert-eagle" or answer.lower() == "deagle":
    print("Correct!!")
    score += 0.5
else:
    print("Incorrect :(")   
    
answer = input("How many guns with 30 bullets per magazine are there? ")
total_questions += 1
if answer == "5":
    print("Correct!!")
    score += 2
else:
    print("Incorrect :(")   

answer = input("What is the highest rank in CSGO? ")
total_questions += 0.5
if answer.lower() == "global elite":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :(")   

answer = input("How many bullets per magazine does an auto-sniper have? ")
total_questions += 1
if answer == "20":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :(")   

answer = input("How many bullets per magazine does a PP-Bizon have? ")
total_questions += 1
if answer == "64":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :(")   

print("The CSGO QUIZZ is over.")
if score >= 3:
    print("Congratulations!! You got " + str(score) + " out of " + str(total_questions) + " points. Which is " + str(score * 100 // total_questions) + "%")
elif score <= 2 and score != 0:
    print("Unlucky, you got " + str(score) + " out of " + str(total_questions) + " points. Which is " + str(score * 100 // total_questions) + "%")
else:
    print("You didn't get a single answer correct. You have to study more!!")