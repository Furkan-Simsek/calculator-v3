# Math Module Calculator
# /-\
# Author: Furkan Şimşek
# github.com/furkan-simsek
import module as funcs
import time
while True:
    print(
        """
        *********************************************************
        *                        Calculator                     *
        *********************************************************
        """
    )
    print("> 1. Addition // 2. Subtraction // 3. Multiplication // 4. Division \n> 5.Ebob // 6. Ekok \n> 7. Square Root // 8. Logarithm // 9. Circle Area \n> 10. Exit")
    choice = int(input("Enter your choice\n >  "))
    if choice == 1:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Addition: ", funcs.add(x, y))
        time.sleep(1)
    elif choice == 2:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Subtraction: ", funcs.sub(x, y))
        time.sleep(1)
    elif choice == 3:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Multiplication: ", funcs.mul(x, y))
        time.sleep(1)
    elif choice == 4:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Division: ", funcs.div(x, y))
        time.sleep(1)
    elif choice == 5:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Ebob: ", funcs.ebob(x, y))
        time.sleep(1)
    elif choice == 6:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Ekok: ", funcs.ekok(x, y))
    elif choice == 7:
        x = int(input("Enter number: "))
        print("Square Root: ", funcs.sqrt(x))
        time.sleep(1)
    elif choice == 8:
        x = int(input("Enter number: "))
        y = int(input("Enter base: "))
        print("Logarithm: ", funcs.log(y, x))
        time.sleep(1)
    elif choice == 9:
        x = int(input("Enter radius: "))
        print("Circle Area: ", funcs.circleArea(x))
        time.sleep(1)
    elif choice == 10:
        break
    else:
        print("Invalid choice")
        time.sleep(1)











