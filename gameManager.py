import random
from encryption import HMAC,keygen
from userHandler import inputHandler
from tableGenerator import *
from diceManager import *


class handleMoves:
  @classmethod
  def startGame(self,compChoice,userChoice,dicesList):
    if compChoice==userChoice:
      handleMoves.userFirst(dicesList)
    else:
      handleMoves.compFirst(dicesList)

  @classmethod 
  def userFirst(self,dicesList):
      print("You got it right. So you start first.")
      userDice=selectDice.userDice(dicesList)
      print("You choose {}".format(userDice))
      compDice=selectDice.compDice(dicesList)
      print("I select {}".format(compDice))
      print("Time for a roll!")
      print("Your turn first")
      userRollRes=handleMoves.handleUserRoll(userDice,compDice)
      print(f'Your roll result is {userRollRes}')
      print("Now my turn")
      compRollRes=handleMoves.handleCompRoll(compDice,userDice,userRollRes)
      print(f'My roll result is {compRollRes}')
      handleMoves.decision(compRollRes,userRollRes) 

  @classmethod
  def compFirst(self,dicesList):
    print("Sorry, wrong guess! I start first.")
    compDice=selectDice.compDice(dicesList)
    print("I select {}".format(compDice))
    print("Now your turn.")
    userDice=selectDice.userDice(dicesList,compDice)
    print("You choose {}".format(userDice))
    print("Time for a roll!")
    compRollRes=handleMoves.handleCompRoll(compDice,userDice)
    print(f'My roll result is {compRollRes}')
    print("Now your turn")
    userRollRes=handleMoves.handleUserRoll(userDice,compDice,compRollRes)
    print(f'Your roll result is {userRollRes}')
    handleMoves.decision(compRollRes,userRollRes)

  @classmethod
  def rollNumber(self,choice1,choice2):
    res=(choice1+choice2)%6
    return res  
  
  @classmethod
  def handleCompRoll(self,compDice,userDice,userRollRes=None):
    compChoice = random.randrange(6)
    print("I selected a random integer between 0 and 5.")
    key=keygen.otk()
    mac=HMAC.getMAC(key,compChoice)
    print("(HMAC={})".format(mac))
    if not userRollRes:
      userChoice=inputHandler.numInput(6,tablegen.userYetToRoll(compDice,userDice))  
    else:
      userChoice=inputHandler.numInput(6,tablegen.compYetToRoll(compDice,userRollRes))
    fairNum=handleMoves.rollNumber(compChoice,userChoice)
    print(f'The fair number generation result is: {fairNum}')
    rollRes=compDice[fairNum]
    return rollRes
  
  @classmethod
  def handleUserRoll(self,userDice,compDice,compRollRes=None):
    compChoice = random.randrange(6)
    print("I selected a random integer between 0 and 5.")
    key=keygen.otk()
    mac=HMAC.getMAC(key,compChoice)
    print("(HMAC={})".format(mac))
    if not compRollRes:
      userChoice=inputHandler.numInput(6,tablegen.userFirst(compDice,userDice))
    else:
      userChoice=inputHandler.numInput(6,tablegen.compFirst(compRollRes,userDice))
    fairNum=handleMoves.rollNumber(compChoice,userChoice)
    print(f'The fair number generation result is: {fairNum}')
    rollRes=userDice[fairNum]
    return rollRes

  @classmethod
  def decision(self,compNum,userNum):
    if compNum>userNum:
      print(f"Sorry, you lost ({compNum}>{userNum}). Better luck next time.")
    elif userNum>compNum:
      print(f"Excellent! You won ({userNum}>{compNum}).")
    else:
      print("Nobody won.")
