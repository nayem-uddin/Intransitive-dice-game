class parseDices:
  @classmethod
  def tempDices(self,dices:list):
    assert len(dices)>2,"At least 3 dices needed (e.g., 1,2,3,4,5,6  1,2,7,8,9,10  5,0,9,10,11,12)"
    return dices


class finalDices:
  @classmethod
  def dicesProcessed(self,dices:list):
    for idx in range(len(dices)):
      try:
        curr=dices[idx].split(",")
        assert len(curr)==6
        curr=list(map(int,curr))
        dices[idx]=curr
      except:
        raise AssertionError("For each dice,\n" 
        "- input integers only\n"
        "- make sure there are exactly 6 integers\n"
        "- seperate the integers using commas, and nothing else\n"
        "(e.g,. 1,2,3,4,5,6)")