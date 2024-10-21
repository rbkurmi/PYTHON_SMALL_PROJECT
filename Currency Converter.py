def currency_converter():
    print("Currency Conversion Rates:")
    print("1 USD = 85 BDT")
    print("1 USD = 0.85 EUR")

    amount = float(input("Enter amount in USD: "))

    choice = input("Convert to (BDT/EUR): ").upper()

    if choice == "BDT":
        converted = amount * 85
        print(f"{amount} USD = {converted:.2f} BDT")
    elif choice == "EUR":
        converted = amount * 0.85
        print(f"{amount} USD = {converted:.2f} EUR")
    else:
        print("Invalid currency choice!")


currency_converter()
