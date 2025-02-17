              # Calculater
def main():
    print("Calculater")
    open = input("Choose, Addition, Subtration, Multiplication, Division Or Q to Quit: ")
    if open.lower() == "addition":
        print("Addition Calculater") # -------------------------------------------------------Addition
        print("--------------------------")
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))

        print("Answer:")
        print(number1 + number2)# Answer
        print("--------------------------")
        main()
    elif open.lower() == "subtraction":
        print("Subtraction Calculater")  # ------------------------------------------------------Subtraction
        print("------------------------")
        subnumber1 = int(input("Number 1: "))
        subnumber2 = int(input("Number 2:"))
        print("Answer:")
        print(subnumber1 - subnumber2)   # Answer
        print("--------------------------")
        main()
    elif open.lower() == "multiplication":
        print("Multiplication Calculater")  # ----------------------------------------Multiplication
        print("------------------------")
        mulnumber1 = int(input("Number 1: "))
        mulnumber2 = int(input("Number 2:"))
        print(mulnumber1*mulnumber2)
        print(mulnumber2 * mulnumber1)# Answer
        print("--------------------------")
        main()
    elif open.lower() == "division":   # ---------------------------------------------Division
        print("Division Calculater")
        print("------------------------")
        divnumber1 = int(input("Number 1: "))
        divnumber2 = int(input("Number 2: "))
        print("Answer:")
        print(divnumber1 / divnumber2)#Answer
        print("-----------------------------")
        main()
    elif open.lower() == "q":
        exit()

    elif open == 'Secret':
        print("My Name is Wayne")

    else:
        print("Error")
        main()

main()
