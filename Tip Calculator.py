def tip_calculator():
    bill = float(input("Enter the total bill: $"))
    tip_percentage = float(input("Enter the tip percentage: "))
    people = int(input("Enter the number of people to split the bill: "))

    tip = (tip_percentage / 100) * bill
    total = bill + tip
    per_person = total / people

    print(f"Total bill including tip: ${total:.2f}")
    print(f"Each person pays: ${per_person:.2f}")

tip_calculator()
