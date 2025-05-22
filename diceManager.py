import random
from tableGenerator import *
from userHandler import *


class selectDice:
  @classmethod
  def compDice(self,dicesList):
    idx=random.randrange(len(dicesList))
    return dicesList.pop(idx)
  
  @classmethod
  def userDice(self,dicesList,compDice=None):
    if not compDice:
      table=tablegen.allDice(dicesList)
    else:
      table=tablegen.oneVall(compDice,dicesList)
    choice=inputHandler.listInput(dicesList,table)
    return dicesList.pop(choice)