# Binary, Denary, Hexadecimal Calculator (Conversion)
#By Jasmine Nowakowska 22/04/16 - 23/04/16
import sys
import math
from time import sleep
choice = None


def denToBin(denaryNum):
    binaryNum = bin(denaryNum)
    binaryList = []
    for digit in binaryNum:
        binaryList.append(digit)
#    print(binaryList)
    del binaryList[:2]
#    print(binaryList)
    binaryNum = ""
    for item in binaryList:
        binaryNum += item

    return binaryNum


def binToDen(binNum):
    denNum = int(binNum, 2)

    return denNum


def denToHex(denaryNum):
    hexNum = hex(denaryNum)
    hexList= []
    for digit in hexNum:
        hexList.append(digit)
    del hexList[:2]
    hexNum = ""
    for item in hexList:
        hexNum += item

    return hexNum


def hexToDen(hexNum):
     denNum = int(hexNum, 16)

     return denNum


def binToHex(binNum):
    denNum = int(binNum, 2)

    hexNum = hex(denNum)
    hexList= []
    for digit in hexNum:
        hexList.append(digit)
    del hexList[:2]
    hexNum = ""
    for item in hexList:
        hexNum += item

    return hexNum


def hexToBin(hexNum):
    denNum = int(hexNum, 16)
    binaryNum = bin(denNum)
    binaryList = []
    for digit in binaryNum:
        binaryList.append(digit)
    del binaryList[:2]
    binaryNum = ""
    for item in binaryList:
        binaryNum += item

    return binaryNum

def askForInput(usedEq1, usedEq2):
    global num1
    global num2
    num1 = int(input("Enter the first number you would like to " + usedEq1 + ":\n"))
    num2 = int(input("Enter the second number you would like to " + usedEq2 + ":\n"))
    
    return num1, num2
    
def addition(add1, add2):
    addTotal = add1 + add2
    return addTotal


def subtraction(subtract1, subtract2):
    subtractTotal = subtract1 - subtract2
    return subtractTotal


def multiplication(multiply1, multiply2):
    multiplyTotal = multiply1 * multiply2
    return multiplyTotal


def division(division1, division2):
    divisionTotal = division1 / division2
    return divisionTotal

def exponent(power1,power2):
    exponentTotal = math.pow(power1,power2)
    return exponentTotal

def squareRoot(squaredNum):
    sqrtTotal = math.sqrt(squaredNum)
    return sqrtTotal

while choice != 0:
    choice = input("""Welcome to the Calculator/ Number Base Converter!
    Choose one of the option in the menu:

0 - Exit
1 - Convert Denary to Binary
2 - Convert Binary to Denary
3 - Convert Denary to Hexadecimal
4 - Convert Hexadecimal to Denary
5 - Convert Binary to Hexadecimal
6 - Convert Hexadecimal to Binary

7 - NORMAL CALCULATOR

\n""")

    if choice == "0":
        sys.exit()
    elif choice == "1":
        denaryInput = int(input("Enter your Denary/ Decimal Number:\n"))
        print(denaryInput, "in Binary =", denToBin(denaryInput))
        sleep(2)
    elif choice == "2":
        binaryInput = input("Enter your Binary Number:\n")
        print(binaryInput, "in Denary =", binToDen(binaryInput))
        sleep(2)
    elif choice == "3":
        denaryInput = int(input("Enter your Denary/ Decimal Number:\n"))
        print(denaryInput, "in Hexadecimal =", denToHex(denaryInput))
        sleep(2)
    elif choice == "4":
        hexInput = input("Enter your Hexadecimal Number: \n")
        print(hexInput, "in Denary =", hexToDen(hexInput))
        sleep(2)
    elif choice == "5":
        binaryInput = input("Enter your Binary Number:\n")
        print(binaryInput, "in Hexadecimal =", binToHex(binaryInput))
        sleep(2)
    elif choice == "6":
        hexInput = input("Enter your Hexadecimal Number: \n")
        print(hexInput, "in Binary =", hexToBin(hexInput))
        sleep(2)
    elif choice == "7":

        calcChoice = None
        while calcChoice != "0":
            calcChoice = input("Please select an operation:\n"
                               "\n"
                               "0 - Exit to Normal Menu\n"
                               "1 - Addition\n"
                               "2 - Subtraction\n"
                               "3 - Multiplication\n"
                               "4 - Division\n"
                               "5 - Powers/ Exponents\n"
                               "6 - Square Root\n"
                               "\n"
                               "\n")

            if calcChoice == "0":
                print("Heading back to the Main Menu!")
                break

            if calcChoice == "1":
                equation = "add"
                equation2 = "add"
                askForInput(equation,equation2)
                print(num1, "+", num2, "=", addition(num1, num2))
                sleep(2)
            elif calcChoice == "2":
                equation = "subtract"
                equation2 = "subtract from"
                askForInput(equation, equation2)
                print(num1, "-", num2, "=", subtraction(num1, num2))
                sleep(2)
            elif calcChoice == "3":
                equation = "multiply"
                equation2 = "multiply by"
                askForInput(equation, equation2)
                print(num1, "*", num2, "=", multiplication(num1, num2))
                sleep(2)
            elif calcChoice == "4":
                equation = "divide"
                equation2 = "divide by"
                askForInput(equation, equation2)
                print(num1, "/", num2, "=", division(num1, num2))
                sleep(2)
            elif calcChoice == "5":
                equation = "multiply by a power"
                equation2 = "be the power/ exponent"
                askForInput(equation, equation2)
                print(str(num1) + "**" + str(num2), "=", exponent(num1, num2))
                sleep(2)
            elif calcChoice == "6":
                num1 = int(input("Enter the number you would like to find the square root for: \n"))
                print("√" + str(num1), "=", squareRoot(num1))
                sleep(2)
