from random import randint

TotalPoints = 0

#generates random guess
def GenerateGuess():
    return(randint(1,10))

#function checks whether passed ComputerGuess, and UserGuess values are equivalent
def CheckGuess(C, U):
    if (C == U):
        return True     #if equal, returns True
    else:
        return False    #if not equal, returns False

#main
def main():
    print("Let's play the number Guessing Game! The computer will randomly select a number, and if you guess it, you win!")
    UserGuess = int(input("Guess a number from 1 to 10: "))   #takes user input, and stores in UserGuess
    ComputerGuess = GenerateGuess()                           #calls function 'GenerateGuess' and stores returned value in ComputerGuess
    global TotalPoints                                        #made 'TotalPoints' global

    if (CheckGuess(ComputerGuess, UserGuess)):                #checks for 'True', then asks user whether they want to continue or not
        TotalPoints = TotalPoints + 5
        print("Congratz! You guessed correctly, and earned +5 points. \nTotal Points Earned: ", TotalPoints)
        UserDecision = str(input("Do you want to play again? Say 'yes' to continue! "))
        if(UserDecision.lower() == "yes"):
            main()
        else:                                                 #if false, prints string and 'TotalPoints'
            print("Thank you for playing! \nTotal Points Earned: ", TotalPoints)

    else:                                                     #if 'CheckGuess' returns False, prints string, and computer's random guess.
        print("Incorrect guess! The computer had randomly selected:", ComputerGuess)
        UserDecision = str(input("Do you want to play again? Say 'yes' to continue! "))
        
        if(UserDecision.lower() == ("yes")):                  #checks if user wants to continue or not
            main()
        else:
            print("Thank you for playing! \nTotal Points Earned:", TotalPoints )

main()
