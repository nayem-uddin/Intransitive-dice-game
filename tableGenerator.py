from prettyTables import Table
from probability import *


class tablegen:
  @classmethod
  def allDice(self,dice):
    table=tablegen.initTable(dice)
    totalDice=len(dice)
    columnData=[0]*totalDice
    for i in range(totalDice):
      for j in range(totalDice):
        columnData[j]=probCal.dieVdie(dice[i],dice[j])
      head=f'Die {i}: '+ tablegen.toStr(dice[i])
      table.add_column(head,columnData)
    return table
  
  @classmethod
  def oneVall(self,selected,others):
    table=tablegen.initTableForOneVAll(selected)
    for die in others:
      prob=probCal.dieVdie(die,selected)
      table.add_column(tablegen.toStr(die),[prob])
    return table

  @classmethod
  def userFirst(self,compDice,userDice):
    table=tablegen.initTable(list(range(6)))
    columnData=[0]*6
    for userChoice in range(6):
      for compChoice in range(6):
        columnData[compChoice]=probCal.userStarts(userChoice,compChoice,userDice,compDice)
      table.add_column(userChoice,columnData)
    return table
  
  @classmethod
  def compFirst(self,compRollRes,userDice):
    res=probCal.compRolled(userDice,compRollRes)
    return f'Winning possibility {res}'

  @classmethod
  def userYetToRoll(self,compDie,userDie):
    table=tablegen.initTable(compDie)
    columnData=[0]*6
    for userChoice in range(6):
      for compChoice in range(6):
        columnData[compChoice]=probCal.compStarts(userChoice,compChoice,userDie,compDie)
      table.add_column(userChoice,columnData)
    return table


  @classmethod
  def compYetToRoll(self,compDie,userRollRes):
    res=probCal.userRolled(compDie,userRollRes)
    return f'Winning possibility {res}'

  @classmethod
  def toStr(self,param):
    if isinstance(param,list):
      return "["+",".join(map(str,param))+"]"
    return str(param)
  
  @classmethod
  def initTable(self,param):
    table=Table()
    table.add_column("User's choice →\nComputer's choice ↓",list(map(tablegen.toStr,param)))
    return table

  @classmethod
  def initTableForOneVAll(self,arr):
    table=Table()
    table.add_column("User's choice →\nComputer's choice ↓",[tablegen.toStr(arr)])
    return table