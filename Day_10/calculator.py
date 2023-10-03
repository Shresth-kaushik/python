
# Operations 

# Add
def add(a,b):
    return a+b

# subtraction
def sub(a,b):
    return a-b

# Multiplication
def multi(a,b):
    return a * b

# Division
def div(a,b):
    return a / b


# Dictionary :
operation = {
    "+": add,
    "-":sub ,
    "*":multi,
    "/":div
}

first  = int(input("Enter the first number "))
# to print the symbol / operations .
for i in operation:
    print(i)

operation_symbol = input("Select the operation symbol")
second = int(input("Enter the second number"))

calculated_function = operation[operation_symbol] 
answer = calculated_function(first ,second)

print(f"{first} {operation_symbol} {second} = {answer}")




