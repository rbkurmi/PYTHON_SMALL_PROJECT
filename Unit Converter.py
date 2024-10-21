def unit_converter():
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Choose conversion (1/2): "))

    if choice == 1:
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is {miles:.2f} miles.")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Invalid choice.")

unit_converter()
