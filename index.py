import sys, random
from encryption import *
from dicePreprocess import *
from userHandler import *
from gameManager import *
from tableGenerator import *

try:
  dices=parseDices.tempDices(sys.argv[1:])
  finalDices.dicesProcessed(dices)
  oneTimeKey=keygen.otk()
  compChoice=random.randrange(2)
  sha3hmac=HMAC.getMAC(oneTimeKey,compChoice)
  print(
    "Let's determine who starts first.\n"
    "I selected a random integer between 0 and 1."
        )
  print("(HMAC={})".format(sha3hmac))
  print("Try to guess my selection. You will start first if you guess it right.")
  userInput=inputHandler.numInput(2)
  handleMoves.startGame(compChoice,userInput,dices)
except AssertionError as e:
  print(e)