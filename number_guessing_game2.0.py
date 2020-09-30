import random
import pyttsx3
mytext = pyttsx3.init()
new_speech = 150
mytext.setProperty('rate',new_speech)
mytext.say("welcom to number guessing game please guess your number between 1 to 10")
mytext.runAndWait()

win_number = random.randint(1,10)
en_number = int(input("guess your number : "))
number_of_attempt = 1

while True:
    if win_number == en_number:
        mytext.say(f"congrachulation you win and your number of attempts is {number_of_attempt}")
        mytext.runAndWait()
        print(f"congrachulation you win and your number of attempts is {number_of_attempt}")
        break
    else:
        if win_number > en_number:
            mytext.say("you are too low try again")
            mytext.runAndWait()
            en_number = int(input("guess your number : "))
            number_of_attempt += 1
        else:
            mytext.say("you are too high try again")
            mytext.runAndWait()
            en_number = int(input("guess your number : "))
            number_of_attempt += 1




