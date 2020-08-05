num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter another number: ")) #user input is str be default. the input is converted to a float value and stored in the variable

def calc():
    if op=="+":
        return num1 + num2
    elif op=="-":
        return num1 - num2
    elif op=="*":
        return num1 * num2
    elif op=="/":
        return num1/num2
    else:
        print("Operator nor valid")

print(calc())