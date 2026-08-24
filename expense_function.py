import json
from datetime import datetime

# Initialize the global list
expense = []


def add_expense():
    try:
        amt = int(input("Enter amount: "))

        if amt > 0:
            ctg = input("Enter category: ").strip().title()
            descp = input("Enter description: ").strip().title()
            date=input("Enter date (DD-MM-YYYY): ").strip()

            if datetime.strptime(date,"%d-%m-%Y"):
                expense.append({
                "amount": amt,
                "category": ctg,
                "description": descp,
                "date":date
            })
            else:
                print("Enter valid date (DD-MM-YYYY)")    

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
        if "date" not in i:
            i["date"]="Unknown"
            print("Date:",i["date"])
        else:
            print("Date:",i["date"])
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

def edit_expense():
    try:
        number=int(input("Enter expense number to edit: "))

        if number<=0:
            print("Please enter a valid expense to edit.")
            return

        index=number-1
        if index>=len(expense):
            print("Expense number doesn't exist")
            return

        print("\n Current Expenses: ")
        print("Amount",expense[index]["amount"])
        print("Category", expense[index]["category"])
        print("Description",expense[index]["description"])
        print("Date",expense[index]["date"])

        print("\n Enter new amount")

        amount=int(input("Enter new amount: "))

        if amount<=0:
            print("Amount must be greater than 0")
            return

        category=input("Enter new category").strip().title()
        description=input("Enter new description").strip().title()
        date=input("Enter new date (DD-MM-YYYY): ").strip()
        datetime.strptime(date,"%d-%m-%Y")

        expense[index]["amount"]=amount
        expense[index]["category"]=category
        expense[index]["description"]=description
        expense[index]["date"]=date

        print("Exepnse update successfully.")

    except ValueError:
        print("Please enter a valid number")

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
            print("Date:",i["date"])
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

            if "date" not in i:
                i["date"]="Unknown"
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
print("4. Edit Expense")
print("5. Total Spending")
print("6. Highest Expense")
print("7. Lowest Expense")
print("8. Filter by Category")
print("9. Save Data")
print("10. Load Data")
print("11. Category Summary")
print("12. Exit")


while True:

    ch = input("Enter your choice: ")

    if ch == "1":
        add_expense()

    elif ch == "2":
        view_expenses()

    elif ch == "3":
        delete_expense()

    elif ch == "4":
        edit_expense()

    elif ch == "5":
        total_spending()

    elif ch == "6":
        highest_expense()

    elif ch == "7":
        lowest_expense()

    elif ch == "8":
        filter_category()

    elif ch == "9":
        save_data()

    elif ch == "10":
        load_data()

    elif ch == "11":
        category_summary()

    elif ch == "12":
        print("Thanks for using this service.")
        break

    else:
        print("Enter a valid choice.")