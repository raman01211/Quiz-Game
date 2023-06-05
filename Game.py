print("Welcome to my computer Quiz!")

playing = input(" Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okay! Let's play :) ")
score=0
answer =input(" What does CPU Stand for? ")
if answer == "central processing unit":
    print('Correct')
    score= score+1
else:
    print('Wrong')


answer =input(" What does GPU Stand for? ")
if answer == "grpahics processing unit":
    print('Correct')
    score= score+1
else:
    print('Wrong')

answer =input(" What does RAM Stand for? ")
if answer == "Random Access Memory":
    print('Correct')
    score= score+1
else:
    print('Wrong')

print("You got " + str(score) + "questions correct! ")


