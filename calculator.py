#--------------------------------------------------
# Advanced Calculator
# Author: Furkan Şimşek
# github.com/furkan-simsek
# -------------------------------------------------
import os
import module as funcs
import time
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Calculator")
while True:
    print(
        """
        *********************************************************
        *                        Calculator                     *
        *********************************************************
        """
    )
    print("> 1. Addition // 2. Subtraction // 3. Multiplication // 4. Division \n> 5.Ebob // 6. Ekok \n> 7. Square Root // 8. Logarithm // 9. Circle Area // 10. Factorial \n> 11. Exit")
    print("*********************************************************")
    choice = input("Enter your choice\n >  ")
    while True:
        if choice == "1": #Example: 1 + 2 = 3
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    """
                    *********************************************************
                    *                        Addition                     *
                    *********************************************************
                    """
                )
                x = input("Enter first number: ")
                y = input("Enter second number: ")
                try:
                    x = float(x)
                    y = float(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            print(f"{x} + {y} = {funcs.add(x, y)}")    # Addition
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "2": #Example: 1 - 2 = -1
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    """
                    *********************************************************
                    *                        Subtraction                  *
                    *********************************************************
                    """
                )
                x = input("Enter first number: ")
                y = input("Enter second number: ")
                try:
                    x = float(x)
                    y = float(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                x = int(input("Enter first number: "))
                y = int(input("Enter second number: "))
                try:
                    x = float(x)
                    y = float(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            print(f"{x} - {y} = {funcs.sub(x, y)}")    # Subtraction
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "3": #Example: 1 * 2 = 2

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    """
                    *********************************************************
                    *                        Multiplication                *
                    *********************************************************
                    """
                )
                x = input("Enter first number: ")
                y = input("Enter second number: ")
                try:
                    x = float(x)
                    y = float(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            print(f"{x} * {y} = {funcs.mul(x, y)}")    # Multiplication
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "4": #Example: 1 / 2 = 0.5
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    """
                    *********************************************************
                    *                        Division                      *
                    *********************************************************
                    """
                )
                x = input("Enter first number: ")
                y = input("Enter second number: ")
                try:
                    x = float(x)
                    y = float(y)
                    if y == 0:
                        print("Cannot divide by 0")
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            print("Division: ", funcs.div(x, y))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "5": #Example: EBOB(5, 10) = 5
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    """
                    *********************************************************
                    *                        EBOB                           *
                    *********************************************************
                    """
                )
                x = input("Enter number: ")
                y = input("Enter number: ")
                try:
                    x = int(x)
                    y = int(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            print("Ebob: ", funcs.ebob(x, y))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "6": # Example: EKOK(5, 10) = 10
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
                *********************************************************
                *                         EKOK                          *
                *********************************************************
                """)
                x = input("Enter first number: ")
                y = input("Enter second number: ")
                try:
                    x = int(x)
                    y = int(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            print("Ekok: ", funcs.ekok(x, y))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "7": # Example: sqrt(4) = 2
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
                *********************************************************
                *                     Square Root                       *
                *********************************************************
                """)
                x = input("Enter number: ")
                try:
                    x = float(x)
                    break
                except ValueError:
                    print("Please enter a number")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            print("Square Root: ", funcs.sqrt(x))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "8": # Example: log(16, 4) = 2
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
                *********************************************************
                *                         Logarithm                     *
                *********************************************************
                """)
                x = input("Enter base: ")
                y = input('Enter number: ')
                try:
                    x = int(x)
                    y = int(y)
                    break
                except ValueError:
                    print("Please enter a number")
                    continue
            print("Logarithm: ", funcs.log(y, x))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "9": # Example: pi * r * 2 = 12 , r= x
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
                *********************************************************
                *                         Square                        *
                *********************************************************
                """)
                x = input("Enter number: ")
                try:
                    x = float(x)
                    break
                except ValueError:
                    print("Please enter a number")
                    continue
            print("Circle Area: ", funcs.circleArea(x))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "10": # Example: 5! = 120
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(""" 
                *********************************************************
                *                      Factorial                        *
                *********************************************************
                """)
                x = input("Enter number: ")
                try:
                    x = float(x)
                    break
                except ValueError:
                    print("Please enter a number")
                    continue
            print("Factorial: ", funcs.factorial(x))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif choice == "11": #Exit
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
            *********************************************************
            *                          Exit                         *
            *********************************************************
            """)
            time.sleep(1.5)
            break
        else: #Invalid choice(Error)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
            *********************************************************
            *                          Error                        *
            *********************************************************
            """)
            print("Invalid choice")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    if choice == "11": #Exit
        break