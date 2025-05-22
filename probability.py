import numpy as np
class probCal:
  @classmethod
  def dieVdie(self,die1,die2):
    die1=np.repeat(die1,6)
    die2=np.tile(die2,6)
    favorable=np.sum(die1>die2)
    return favorable/36
  
  @classmethod
  def userStarts(self,userChoice,compChoice,userDice,compDice):
    idx=(userChoice+compChoice)%6
    compDice=np.array(compDice)
    return np.sum(userDice[idx]>compDice)/6
  
  @classmethod
  def compRolled(self,userDice,compRes):
    userDice=np.array(userDice)
    return np.sum(userDice>compRes)/6
  
  @classmethod
  def compStarts(self,userChoice,compChoice,userDice,compDice):
    idx=(userChoice+compChoice)%6
    userDice=np.array(userDice)
    return np.sum(userDice>compDice[idx])/6

  @classmethod
  def userRolled(self,compDice,userRes):
    compDice=np.array(compDice)
    return np.sum(compDice<userRes)/6
