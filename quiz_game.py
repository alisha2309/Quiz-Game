print("WELCOME TO THE QUIZ GAME!!")
playing=input("Do you want to play the game? ")
if playing.lower() != "yes":
    quit()
print("Ok! Lets play the game :) ")
print("Enter your name: ")
name=input()
print("Hello {}".format(name))
score=0
answer = input("1. What does cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("2. What does gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("3. What does ram stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("4. What does psu stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(str(name)+" You got " +str(score)+ " questions correct!")
print(str(name)+" You got " +str((score/4)*100)+ " %")
