# Quiz game
print("Welcome to my computer quiz !")

playing = input("Do you want to play? ")

if playing.upper() != "YES": #upper = colocar todas as letras em caixa alta
    quit()

print("Okay! Let's play :)")
score = 0

#first question
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Second question
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Third question
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Fourth question
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 4) * 100) + "%.")
