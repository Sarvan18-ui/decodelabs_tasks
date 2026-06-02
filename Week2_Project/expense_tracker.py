# Decode Labs Week 2 - Expense Tracker

expenses = []
total = 0

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add expense
    if choice == "1":
        amount = float(input("Enter expense amount: "))

        expenses.append(amount)
        total = total + amount

        print("Expense added successfully!")

    # View all expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added")

        else:
            print("\nExpenses:")
            for i in range(len(expenses)):
                print(f"{i+1}. {expenses[i]}")

    # View total
    elif choice == "3":
        print(f"\nTotal Spent: {total}")

    # Exit
    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice")