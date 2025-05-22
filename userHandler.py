class inputHandler:
  @classmethod
  def listInput(self,arr,helpTable):
    while True:
      inputHandler.inputManager(arr)
      n=input("Enter your choice: ").capitalize()
      assert n!="X","Thanks for playing"
      if n=="?":
        print(helpTable)
      elif n.isdigit() and int(n)<len(arr):
        return int(n)
      else:
        print("Enter a valid input")
        continue

  @classmethod
  def numInput(self,stop,helpTable="Winning possibility: 0.5"):
    while True:
      inputHandler.inputManager(list(range(stop)))
      n=input("Enter your choice: ").capitalize()
      assert n!="X","Thanks for playing"
      if n=="?":
        print(helpTable)
      elif n.isdigit() and int(n)<stop:
        return int(n)
      else:
        print("Enter a valid input")
        continue

  @classmethod
  def inputManager(self,items):
    for idx,ele in enumerate(items):
      print(f'{idx} - {ele}')
    print("X - exit\n? - help")