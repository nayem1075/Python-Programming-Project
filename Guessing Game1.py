import random

for x in range(1,10):

      guessNumber = int(input("Enter any number between (1-100) : "))
      randomNumber = random.randint(1,100)

      print("Random Number is : ",randomNumber)

      if guessNumber == randomNumber:
       print("Congratulation! You Won")
      else:
        print("You Lost")