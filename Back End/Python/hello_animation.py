import os
import time


def animate_text(text):
  numberOfCharacters=1
  while True:
    print("\n")
    print(text[0:numberOfCharacters])
    numberOfCharacters += 1
    if numberOfCharacters > len(text):
      numberOfCharacters = 0
    time.sleep(0.5)
    os.system('clear')


#Main Program Starts Here....
animate_text('\033[91m' + "Hello World!" +'\033[0m')
#color unicode:
#https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
