# Computer Quiz name

print("Hello welcome to my quiz!")
play = input("Do you want to play? ")
if play.lower() == 'yes':
    print("Come on let's play!")
else:
    quit()

score = 0

question= input("Who invented Java? ")
if question.lower() == "james a gosling":
    print("Yes, that's right!")
    score += 1
else:
    print("OH! You are incorrect!")
    print("The right answer is: " + "james a gosling")

question= input("What is the expansion of SMS? ")
if question.lower() == "short message service":
    print("Yes, that's correct!")
    score += 1
else:
    print("OH! You are incorrect!")
    print("The right answer is: " + "short message service")

question= input("'Do no evil' is tag line of ")
if question.lower() == "google":
    print("You're dead right!")
    score += 1
else:
    print("OH! You are incorrect!")
    print("The right answer is: " + "google")

question= input("Expand RDBMS? ")
if question.lower() == "relational data base management system":
    print("Absolutely!")
    score += 1
else:
    print("OH! You are incorrect!")
    print("The right answer is: " + "relational data base management system")

question= input("What is SQL? ")
if question.lower() == "structured query language":
    print("You've hit the nail on the head!")
    score += 1
else:
    print("OH! You are incorrect!")
    print("The right answer is: " + "structured query language")

print("Great! You have answered " + str(score) + " questions correctly.")
print("You got " + str((score/5)*100) + "%")


