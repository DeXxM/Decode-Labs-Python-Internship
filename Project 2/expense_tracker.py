"""
Project 2: Expense Tracker
DecodeLabs Python Programming Internship
"""

expenses = []
total = 0.0

print("=" * 40)
print("          EXPENSE TRACKER")
print("=" * 40)
print("Enter an expense amount (e.g. 100 or 50.50).")
print("Type 'quit' to finish and view your total.")
print("-" * 40)

while True:
    user_input = input("Enter expense amount: ").strip()

    # Stop the loop when the user enters 'quit'
    if user_input.lower() == "quit":
        break

    # Convert input into a number and handle invalid entries
    try:
        new_expense = float(user_input)

        if new_expense <= 0:
            print("Please enter an amount greater than zero.")
            continue

    except ValueError:
        print("Invalid input. Enter a number, such as 100 or 50.50.")
        continue

    # Store the expense and update the running total
    expenses.append(new_expense)
    total = total + new_expense

    print(f"Expense added: {new_expense:.2f}")
    print(f"Running total: {total:.2f}")
    print("-" * 40)

# Display the final summary
print("\n" + "=" * 40)
print("             EXPENSE SUMMARY")
print("=" * 40)

if len(expenses) == 0:
    print("No expenses were entered.")
else:
    for number, amount in enumerate(expenses, start=1):
        print(f"{number}. {amount:.2f}")

    print("-" * 40)
    print(f"Number of expenses : {len(expenses)}")
    print(f"TOTAL SPENT        : {total:.2f}")

print("=" * 40)
print("Thank you for using Expense Tracker!")
