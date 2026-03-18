while True:
    try:
        number = float(input("Enter a float number: "))
        print("You entered:", number)
        break   # exit loop if correct

    except ValueError:
        print("Invalid input! Please enter a valid float number.\n")

