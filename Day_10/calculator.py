
# # Operations 

# # Add
# def add(a,b):
#     return a+b

# # subtraction
# def sub(a,b):
#     return a-b

# # Multiplication
# def multi(a,b):
#     return a * b

# # Division
# def div(a,b):
#     return a / b


# # Dictionary :
# operation = {
#     "+": add,
#     "-":sub ,
#     "*":multi,
#     "/":div
# }

# first  = int(input("Enter the first number "))
# # to print the symbol / operations .
# for i in operation:
#     print(i)

# operation_symbol = input("Select the operation symbol")
# second = int(input("Enter the second number"))

# calculated_function = operation[operation_symbol] 
# answer = calculated_function(first ,second)

# print(f"{first} {operation_symbol} {second} = {answer}")




# -------------->> OPTIMIZED CODE OF THE CALCULATOR <<--------------------
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator() #recursive call -> so that function can start form scratch/inital stage.

# calulator function form kiya hai .
calculator()


