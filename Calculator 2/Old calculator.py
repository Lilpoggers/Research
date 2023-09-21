#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtact
def subtract(n1, n2):
  return n1 - n2
    
#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Centimeter
def centimeter(n1):
  return n1 / 2.54

#Inches
def inches(n1):
   return n1 * 2.54

def clear():
  return

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "cm": centimeter,
  "in": inches,
  "c": clear
  }

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
    
  operation_symbol = input("Pick an operation: ")

  if operation_symbol == "cm":
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1)
    print(f"{num1} {operation_symbol} = {answer}")

  elif operation_symbol == "in":
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1)
    print(f"{num1} {operation_symbol} = {answer}")

  elif operation_symbol == "c":
    return(print("cleared"))

  else:
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

calculator()