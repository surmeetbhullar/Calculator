i = 0

def mainmenu():
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. Quit")

def calculate(numb1, numb2, option):
    result = None  # Initialize the result variable
    if option == 1:
        result = numb1 + numb2
    elif option == 2:
        result = numb1 - numb2
    elif option == 3:
        result = numb1 * numb2
    elif option == 4:
        result = numb1 / numb2
    elif option == 5:
        print("You have quit the program.")
        result = 0
    else:
      print("Please select a # between 1-4.")
    return result


while i == 0:
  num1 = float(input("Please enter the first number: "))  # Corrected input statement
  num2 = float(input("Please enter the second number: "))  # Corrected input statement

  mainmenu()  # Removed unnecessary print statement
  options = int(input("Please select an operation: "))  # Corrected input statement
  if options == 5:
    i = 1
  result = calculate(num1, num2, options)  # Store the calculated result

  output = "The result is %s." % result  # Use the calculated result in the output string
  print(output)