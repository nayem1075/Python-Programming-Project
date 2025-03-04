import random

for x in range(1,6):

    guessNumber = int(input("Enter your gues between (1-5) : "))
    randomNumber = random.randint(1,5)  #For big number random.random()*100 mean (0-99)

    print("Random Number is : ",randomNumber)

    if guessNumber == randomNumber:
        print("Congratulation! You Won")
    else:
        print("You Lost")



