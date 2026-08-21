import json

# Initialize the global list if it doesn't already exist
expense = []


def add_expense():
    amt = int(input("Enter amount: "))
    ctg = input("Enter category: ")
    descp = input("Enter description: ")
    expense.append({"amount": amt, "category": ctg, "description": descp})


def view_expenses():
    for i in expense:
        print("Amount:", i["amount"])
        print("Category:", i["category"])
        print("Description:", i["description"])
        print()


def delete_expense():
    dlt = int(input("Enter expense number to delete: "))
    del expense[dlt]
    print(expense)


def total_spending():
    total = 0
    for i in expense:
        total += i["amount"]
    print(f"Total spending is {total}")
    print()


def highest_expense():
    highest = 0
    for i in expense:
        if i["amount"] > highest:
            highest = i["amount"]
    print("Highest expense is ", highest)


def lowest_expense():
    if not expense:
        print("No expenses found.")
        return
    lowest = expense[0]["amount"]
    for i in expense:
        if i["amount"] < lowest:
            lowest = i["amount"]
    print("Lowest expense is ", lowest)


def filter_category():
    search = input("What you are looking for ")
    for i in expense:
        if i["category"] == search:
            print("Amount:", i["amount"])
            print("Category:", i["category"])
            print("Description:", i["description"])
            print()


def save_data():
    with open("expense.json", "w") as f:
        json.dump(expense, f)


def load_data():
    global expense
    with open("expense.json", "r") as f:
        expense = json.load(f)

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
print("10. Exit")