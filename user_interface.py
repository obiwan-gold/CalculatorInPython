class UserInterface: 
  def __init__(self, firstNumber, secondNumber, operator):
    self.firstNumber = firstNumber
    self.secondNumber = secondNumber
    self.operator = operator 

    def getUserInputForNumbers(self):
      userFirstNumberInput = input("Enter the first number: ")
      userSecondNumberInput = input("Enter the second number: ")

    def getUserInputForOperator(self):
      userSelectedOperator = input("""Select the operator:
                                      + for addition,
                                      - for subtraction,
                                      * for multiplication,
                                      / for division: """)
      checkOperator(userSelectedOperator)
      
    def checkOperator(self): 
      if userSelectedOperator == +:
        print("hello")
      

