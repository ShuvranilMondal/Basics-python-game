import random
win_number = random.randint(0,10)
guess = 1                                                                       # calculate your number of attempts 
number = int(input("Enter your number between 0 to 10 : "))
game_over = False                                                               # initial  time it would be false

while not game_over:
    if number == win_number:
        print(F"Congraction you win !!\nand your guess time : {guess}")
        game_over = True                                                        # break the loop 
    else:
        if number < win_number:
            print("you are too low !!")
            number = int(input("Try agian :"))
            guess += 1
        else:
            print("Too high !! : ")
            number = int(input("Try again "))
            guess += 1