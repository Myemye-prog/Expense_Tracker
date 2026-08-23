import json

# Initialize the global list
expense = []


def add_expense():
    try:
        amt = int(input("Enter amount: "))

        if amt > 0:
            ctg = input("Enter category: ").strip().title()
            descp = input("Enter description: ").strip().title()

            expense.append({
                "amount": amt,
                "category": ctg,
                "description": descp
            })

            print("Expense added successfully.")

        else:
            print("Enter an amount more than 0")

    except ValueError:
        print("Please enter a valid number.")


def view_expenses():
    if not expense:
        print("No expenses found.")
        return

    for number, i in enumerate(expense, start=1):
        print(number, "Amount:", i["amount"])
        print("Category:", i["category"])
        print("Description:", i["description"])
        print()


def delete_expense():
    try:
        dlt = int(input("Enter expense number to delete: "))
        print()

        if dlt > 0:
            del expense[dlt - 1]

            print("Expense deleted successfully.")
            view_expenses()

        else:
            print("Please enter a valid expense number.")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Expense number doesn't exist.")


def total_spending():
    if not expense:
        print("No expenses found.")
        return

    total = 0

    for i in expense:
        total += i["amount"]

    print(f"Total number of expenses: {len(expense)}")
    print(f"Total spending is: {total}")
    print()


def highest_expense():
    if not expense:
        print("No expenses found.")
        return

    highest = expense[0]["amount"]

    for i in expense:
        if i["amount"] > highest:
            highest = i["amount"]

    print("Highest expense is:", highest)


def lowest_expense():
    if not expense:
        print("No expenses found.")
        return

    lowest = expense[0]["amount"]

    for i in expense:
        if i["amount"] < lowest:
            lowest = i["amount"]

    print("Lowest expense is:", lowest)


def filter_category():
    search = input("What are you looking for? ").strip().title()

    if search == "":
        print("Input can't be empty.")
        return

    found = False

    for i in expense:
        if i["category"] == search:
            found = True

            print("Amount:", i["amount"])
            print("Category:", i["category"])
            print("Description:", i["description"])
            print()

    if not found:
        print("No expenses found for this category.")


def category_summary():
    if not expense:
        print("No expenses found.")
        return

    summary = {}

    for i in expense:

        if i["category"] in summary:
            summary[i["category"]] += i["amount"]

        else:
            summary[i["category"]] = i["amount"]

    print("\nCategory Summary:")

    for category, amount in summary.items():
        print(category, ":", amount)

    print()


def save_data():
    try:
        with open("expense.json", "w") as f:
            json.dump(expense, f, indent=4)

        print("Data saved successfully.")

    except PermissionError:
        print("Permission denied. Unable to save data.")


def load_data():
    global expense

    try:
        with open("expense.json", "r") as f:
            expense = json.load(f)

        # Convert existing data to title case
        for i in expense:
            i["category"] = i["category"].strip().title()
            i["description"] = i["description"].strip().title()

        print("Loaded successfully.")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Expense file contains invalid data.")

    except PermissionError:
        print("Permission denied. Unable to load data.")


print("===== EXPENSE TRACKER =====")
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Total Spending")
print("5. Highest Expense")
print("6. Lowest Expense")
print("7. Filter by Category")
print("8. Save Data")
print("9. Load Data")
print("10. Category Summary")
print("11. Exit")


while True:

    ch = input("Enter your choice: ")

    if ch == "1":
        add_expense()

    elif ch == "2":
        view_expenses()

    elif ch == "3":
        delete_expense()

    elif ch == "4":
        total_spending()

    elif ch == "5":
        highest_expense()

    elif ch == "6":
        lowest_expense()

    elif ch == "7":
        filter_category()

    elif ch == "8":
        save_data()

    elif ch == "9":
        load_data()

    elif ch == "10":
        category_summary()

    elif ch == "11":
        print("Thanks for using this service.")
        break

    else:
        print("Enter a valid choice.")
