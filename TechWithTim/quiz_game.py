print("Basavaraju!, Welcome to the Projets with TWT!")

playing = input("Do you want to play? ")
Score = 0

if playing.lower() != "yes":
    quit()

print("Okay Lets Play Smiley Face")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

print("You got " + str(Score) + " questions correct!")

print("You got " + str((Score/4)*100) + "%")
