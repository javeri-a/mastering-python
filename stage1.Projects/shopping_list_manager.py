print("════════════════════════════════════")
print("       🛒 SHOPPING LIST MANAGER      ")
print("════════════════════════════════════")

shopping_list = []

while True:
    print("\nChoose an option:")
    print(" [1] ➕ Add item")
    print(" [2] ❌ Remove item")
    print(" [3] 📋 View list")
    print(" [4] 🚪 Exit")

    choice = input("\n➤ Enter your choice: ")

    if choice == "1":
        item = input("➤ Enter item to add: ").strip().title()
        shopping_list.append(item)
        print(f"✅ {item} added to the list.")

    elif choice == "2":
        item = input("➤ Enter item to remove: ").strip().title()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"❌ {item} removed from the list.")
        else:
            print(f"⚠ {item} not found in the list.")

    elif choice == "3":
        print("\n📝 Your Shopping List:")
        print("════════════════════════════════════")
        if len(shopping_list) == 0:
            print("⚠ List is empty.")
        else:
            for i, item in enumerate(shopping_list, start=1):
                print(f" {i}. {item}")
        print("════════════════════════════════════")

    elif choice == "4":
        print("\n👋 Exiting... Goodbye!")
        print("════════════════════════════════════")
        break

    else:
        print("⚠ Invalid choice, try again.")
