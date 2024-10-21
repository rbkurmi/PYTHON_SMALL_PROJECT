def shopping_list():
    items = []

    while True:
        print("\n1. Add item\n2. Remove item\n3. View list\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            item = input("Enter item to add: ")
            items.append(item)
            print(f"{item} added to the list.")
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in items:
                items.remove(item)
                print(f"{item} removed from the list.")
            else:
                print("Item not found.")
        elif choice == '3':
            print("Your shopping list:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

shopping_list()
