# Calculator function

# Adding
def add(n1,n2):
  return n1 + n2

# Subtracting
def subtract(n1,n2):
  return n1 - n2

# Dividing 

def divide(n1,n2):
  if n1 or n2 == 0:
    return "Error Can't Divide by 0"
  return n1/n2

# Multiplying

def multiply(n1,n2):
  return n1*n2

# Made a dictionary based on the operations. 
operations = {
 '+':add,
 '-':subtract,
 '/':divide,
 '*':multiply 
}

# While loop to calculate everything.

calculator_loop = True

while calculator_loop:
  num1 = int(input("Please enter the first number: "))
  for opr in operations:
    print(opr)
  opr_sign = input("Select the operator above:")
  num2 = int(input("Please enter the second number: "))
    
  if opr_sign == '+':
    add(num1,num2)
    print(f"{num1} {opr_sign} {num2} equals {add(num1,num2)}")
  elif opr_sign == '-':
    subtract(num1,num2)
    print(f"{num1} {opr_sign} {num2} equals {subtract(num1,num2)}")
  elif opr_sign == '/':
    divide(num1,num2)
    print(f"{num1} {opr_sign} {num2} equals {divide(num1,num2)}")
  elif opr_sign == '*':
    multiply(num1,num2)
    print(f"{num1} {opr_sign} {num2} equals {multiply(num1,num2)}")
  else:
    print("You have selected an invalid entry. Try again.")
  keepitgoing = input("Would you like to continue? (y/n):\n")
  if keepitgoing == 'y':
    continue
  elif keepitgoing == 'n':
    break
  else:
    print("You made an invalid entry. Restarting program...\n")





    




