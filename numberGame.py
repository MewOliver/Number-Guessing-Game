
import random
import time


print("A random number between 1 and 10 will be selected")
print("You have three guesses to get the right number")
play = True
streak = 0
hs = 0
while play == True:
    answer = random.randrange(1,10)
    guess = 0
    win = False


    while guess < 3 and win == False:
        cont = True
        while cont is True:
            try:
                number = int(input("Type a number "))
                cont = False
                print('-----------')
            except:
                print('Please type a number')
        if number == answer:
            print("Congradulations, You Win")
            guess = guess+1
            win = True

        else: 
            print("Try Agian")
            guess = guess+1
            print("Used Guesses: ", guess)
            if number > answer:
                print("Too high")
            else:
                print("Too Low")

    if guess == 3 and win == False:
        print("You Lose")
        print("The answser was: ", answer)
        streak = 0
        play = False

    if win == True:
        streak = streak+1
        print("Your guess count was: ", guess)
        print("Your current streak is: ", streak)
        if streak > hs:
            hs = streak
        play = False

    if play == False:
        again = False
        while again == False:
            restart = input("Would you like to play again: ")
            if restart == "yes":
                play = True
                again = True
            elif restart == "no":
                print("Thanks for playing")
                print("Your best streak was: ", hs)
                again = True
                time.sleep(60)
            else:
                print("Please type 'yes' or 'no'")
                play = False
                again = False
if play and again == False:
    quit()

