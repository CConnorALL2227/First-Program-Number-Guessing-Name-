
import random
import keyboard
import time
import os
import subprocess
import sys

play_again_choice = True
attempts = 0
i = 0
z = 1
reward = False
hotkeyPressed = False
myNum = 0
x = False
key = 'y'


def on_hotkey(String):
    global i, x, hotkeyPressed, reward
    if hotkeyPressed == False:
        if (String == 'e'):
            i = 5
            print("Difficulty set to Easy, you have 5 guesses.")
            x = True
        elif (String == 'm'):
            i = 3
            print("Difficulty set to Medium, you have 3 guesses.")
            x= True
        elif (String == 'h'):
            i = 0
            reward = True
            print("Difficulty set to Hard, you only have 1 guess. Good Luck")
            x = True
        hotkeyPressed = True

def get_guess():
    global myNum
    print("Type a number 0 - 5, try to match with the computer!")
    while True:
        myNum = keyboard.read_key(suppress=True)
        time.sleep(0.1)
        if myNum in ['0', '1', '2', '3', '4', '5']:
            return int(myNum)

def play_game():
    global attempts, myNum, i, x, hotkeyPressed, reward, play_again_choice, key
    while play_again_choice:
        attempts = 0
        i = 0
        x = False
        reward = False
        hotkeyPressed = False
        os.system('cls' if os.name == 'nt' else 'clear')

        keyboard.unhook_all()
        keyboard.add_hotkey('e', on_hotkey, suppress=True, args=('e'))
        keyboard.add_hotkey('m', on_hotkey, suppress=True, args=('m'))
        keyboard.add_hotkey('h', on_hotkey, suppress=True, args=('h'))
        print("Press \"e\" for Easy difficulty, \"m\" for Medium, and \"h\" for Hard")
        while not x:
            time.sleep(0.1)

        Turns = 0
        computerNumber = random.randint(0, 5) 
      #  print(computerNumber)  # uncheck for debugging purposes
        while (Turns <= i):
            try: 
                myNum = get_guess()
                Turns += 1
                attempts += 1
                if (myNum == computerNumber):
                    print("  The Number was the same!")
                    if (reward == True):
                        print("   Amazing! You did it on hard!")
                    elif (attempts == 1):
                        print("   First Try! Nice job!")
                    break
                else:
                    print("The number was not the same...", end=" ")
                    if Turns < i - 1:
                        print("Try again!")
                    elif Turns == i - 1:
                        print("Last Chance!")
            except ValueError:
                print("That wasnt a number")
        if myNum != computerNumber:
            print("Better Luck Next Time...")

        time.sleep(0.5)
        keyboard.unhook_all()
        print("Press 'y' to play again, or 'n' to stop")
        while True:
            key = keyboard.read_key(suppress=True)
            if key == 'y':
                os.execv(sys.executable, [sys.executable, 'firstday.py'])
                key = 'n'
                break
            elif key == 'n':
                print("Thanks for playing!")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.exit(0)
                break
play_game()