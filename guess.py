# """
#  *****************************************************************************
#    FILE:        guess.py
#
#    AUTHOR:      {Midori Knecht}
#
#    ASSIGNMENT:  Mind Reader
#
#    DATE:        June 23, 2022
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************
# randrange(1000,10000) : Gives a random four digit numbers.
from random import randrange


# Define your function guessing_game below. All of your logic/code for playing the game should be written
# in your function guessing_game.
def guessing_game(num): 
  continue_playing = True
  output = ""
  attempts = 1
  numCorrect = 0
  guess = input("Guess the 4-digit number: ")

  while num != guess:
    numCorrect = 0
    output = ""
    
    for i in range(4):
      if num[i] == guess[i]:
        output += num[i]
        numCorrect += 1
      else: 
        output += "X"

    if numCorrect == 1:
      print("Not quite the number. But you did get 1 digit right")
      print(output)
      guess = input("Enter your next choice of numbers: ")
    elif numCorrect == 0:
      print("None of the numbers in your guess match.")
      guess = input("Enter your next choice of numbers: ")
    else:
      print(f"Not quite the number. But you did get {numCorrect} digits right")
      print(output)
      guess = input("Enter your next choice of numbers: ")

    attempts += 1

  if num == guess and attempts == 1:
    print("Wow! You guessed the number in just 1 try! You're lucky!")
  else: 
    print(f"That's a match! It took you only {attempts} tries.")

  keep_playing = input("Do you want to continue playing? (Y/N) ").upper()

  if keep_playing == "Y":
    main()

  
def main():
  randNum = str(randrange(1000,9999))
  guessing_game(randNum)


##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()